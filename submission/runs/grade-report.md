# Tự kiểm tra sự cố S1 · PASS-VISIBLE (chưa chạy test ẩn)

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S1-grade-20261119-175905-e439d2` · bàn: `K5-L3B-DAY10-HiLab-PoCtoPilotGate1` · grader `lab10-1.0` · 1.319s
- Ba mốc: base `R-S1-before-20261119-175907-e439d2` · prepared `R-S1-prepared-20261119-175907-e439d2` · after `R-S1-after-20261119-175907-e439d2` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `42bfd853`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `e439d2f803aa`
- Hash Bản tiêu chí chấp nhận: `66c81588cb6d` · đã ký: `66c81588cb6d` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S1` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: S1 · khớp

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ✅ | file khoá bị đổi: không |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ✅ | base có vấn đề: True; after sạch: True; ticket còn hỏng: không; trần còn vượt: không |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['carrier_fault_rate', 'model_override_rate']; sáng đèn: [('carrier_fault_rate', 'before', 0.509091, 0.846154), ('carrier_fault_rate', 'after', 0.384615, 0.75), ('model_override_rate', 'before', 0.045455, 0.461538)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.0 | 0.0 | 0.0 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 0 |
| chi phí mỗi ticket (đ) · làm tay | 2964 · 10000 | 2964 · 10000 | 4390 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 669 · 1500 | 669 · 1500 | 669 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | -105531 | -105531 | 44880 |
| ROI | -2.74 | -2.74 | 1.28 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 110000 · 2000000 | 110000 · 2000000 | 38000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 197000 · 2000000 | 197000 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 1.0 | 0.6154 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 30 | 30 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 0.0; hoàn sai 275000; oan 15; PII 0; chi phí 662đ | pass 0.0; hoàn sai 275000; oan 15; PII 0; chi phí 662đ | — |
| kho DN | pass 0.0; hoàn sai 120000; oan 5; PII 0; chi phí 664đ | pass 0.0; hoàn sai 120000; oan 5; PII 0; chi phí 664đ | — |
| kho HCM | pass 0.3333; hoàn sai 100000; oan 5; PII 0; chi phí 633đ | pass 0.3333; hoàn sai 100000; oan 5; PII 0; chi phí 633đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 633đ |
| kho HN | pass 0.6; hoàn sai 490000; oan 5; PII 0; chi phí 664đ | pass 0.6; hoàn sai 490000; oan 5; PII 0; chi phí 664đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 644đ |
| hãng DNB | pass 0.0; hoàn sai 120000; oan 0; PII 0 | pass 0.0; hoàn sai 120000; oan 0; PII 0 | — |
| hãng GHSH | pass 0.3636; hoàn sai 865000; oan 30; PII 0 | pass 0.3636; hoàn sai 865000; oan 30; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.0; hoàn sai 0; oan 0; PII 0 | pass 0.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.2273 | 0.2308 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 0 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 4203 · 10000 | 5165 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 670 · 1500 | 670 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 123542 | 62850 |
| ROI | 1.34 | 1.34 | 0.94 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 20000 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 1.0 | 0.5909 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 1 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | — |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | — |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2567đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1994đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | — |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | — |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- Không vượt trần kinh doanh / vận hành nào.
- Mọi ngưỡng đã ký đều đạt.
- Được phép cân nhắc 'Tiếp tục'.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 0.9909 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 0.9545 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 20000 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 1 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.2273 | 0.2308 | +0.0035 |
| visible | pass_rate | 0.3077 | 0.3077 | 1.0 | +0.6923 |
| visible | pass_k | 0.3077 | 0.3077 | 1.0 | +0.6923 |
| visible | wrongful_refund_vnd | 985000 | 985000 | 0 | -985000 |
| visible | under_refund_vnd | 105000 | 105000 | 0 | -105000 |
| visible | wrongful_carrier_faults | 30 | 30 | 0 | -30 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 0 | 0 | 0 | +0 |
| visible | escalation_rate | 0.0 | 0.0 | 0.0 | +0.0 |
