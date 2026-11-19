"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
import re
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Cổng 0: Ghim phiên bản chính sách có hiệu lực tại ngày ctx.as_of
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    policy_id = policy["policy_id"] if policy else None

    # Kiểm tra tính toàn vẹn dữ liệu vận đơn: Đã giao nhưng thiếu ngày giao -> chuyển người duyệt
    order_id = ctx.ticket.get("order_id")
    if order_id:
        order = ctx.tools.lookup_order(order_id)
        if order:
            for p in order.get("parcels", []):
                if p.get("status") == "DELIVERED" and not p.get("delivered_date"):
                    return Verdict.escalate("Dữ liệu vận đơn chưa đồng bộ: kiện hàng ghi đã giao nhưng thiếu ngày giao")

    # Cổng tiền xử lý: Loại bỏ số ngày khách tự khai để model không override số ngày thực tế từ Tracking DB
    text = ctx.ticket.get("text", "")
    clean_text = re.sub(
        r"((?:trễ|tre|chậm|muộn|late|delay(?:ed)?)\D{0,24}?)\d{1,3}(\s*(?:ngày|ngay|days?|hôm))",
        r"\1mấy\2",
        text,
        flags=re.I,
    )
    if clean_text != text:
        return Verdict.rewrite("Loại bỏ số ngày khách tự khai để chống model_override", clean_text, policy_id=policy_id)

    if policy_id:
        return Verdict.allow(policy_id=policy_id)
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    # Cổng 1: Chặn hoàn tiền sai dựa trên Source of Truth (Tracking DB)
    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id") or ctx.ticket.get("order_id"))
        if order:
            parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
            policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
            db_delay = H.db_delay_days(parcel, ctx.as_of)
            entitled = H.entitlement_vnd(policy, order, db_delay, parcel.get("delay_cause"))

            # Nếu đơn không đủ điều kiện trễ theo DB -> từ chối hoàn tiền
            if entitled == 0 and action.get("amount_vnd", 0) > 0:
                return Verdict.deny("Tracking DB ghi nhận đơn không đủ điều kiện trễ để hoàn tiền")

            # Nếu số tiền yêu cầu hoàn vượt quyền lợi thực tế -> điều chỉnh về đúng quyền lợi DB
            if action.get("amount_vnd", 0) > entitled:
                return Verdict.modify("Điều chỉnh số tiền hoàn về đúng mức quyền lợi theo DB", amount_vnd=entitled)

    # Cổng 2: Chặn ghi lỗi oan cho hãng vận chuyển (Carrier fault)
    if tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id") or ctx.ticket.get("order_id"))
        if order:
            parcel = next((p for p in order.get("parcels", []) if p["parcel_id"] == action.get("parcel_id")), None) \
                or H.ticket_parcel(order, ctx.ticket, ctx.as_of)
            policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
            db_delay = H.db_delay_days(parcel, ctx.as_of)
            if not H.carrier_at_fault(policy, parcel, db_delay):
                return Verdict.deny("Tracking DB không ghi nhận nguyên nhân chậm do hãng vận chuyển")

            # Giới hạn số lỗi ghi phạt tự động cho một hãng mỗi ngày (ops_limits)
            carrier_id = action.get("carrier_id")
            strikes_today = len(ctx.tools.fault_rows(carrier_id=carrier_id))
            max_strikes = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day", 2)
            if strikes_today >= max_strikes:
                return Verdict.deny(f"Hãng {carrier_id} đã chạm trần {max_strikes} lỗi tự động trong ngày")

    # Cổng 3: Chặn rò rỉ dữ liệu cá nhân (PII) khi gửi thông báo cho bên thứ ba (Hãng)
    if tool == "notify_carrier":
        payload = action.get("payload", {})
        if "recipient_contact" in payload:
            clean_payload = {k: v for k, v in payload.items() if k != "recipient_contact"}
            return Verdict.modify("Bảo vệ PII: loại bỏ thông tin liên hệ người nhận trước khi gửi bên thứ ba", payload=clean_payload)

    return Verdict.allow()


