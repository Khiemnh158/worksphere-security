# Phạm vi An toàn thông tin (đề xuất, chưa có rubric chính thức)

| Trọng tâm | Việc phải làm | Minh chứng |
| --- | --- | --- |
| Mô hình đe dọa | DFD client/API/DB/file/pipeline; tài sản, tác nhân, STRIDE | Threat model và quyết định kiểm soát |
| Xác thực/session | Logout token cũ, rotation một lần, tài khoản khóa, policy đổi mật khẩu | Test trước/sau F03/F04/F15/F33 |
| Phân quyền đối tượng | PM không sửa project khác; coordinator chỉ team; requester/agent đúng state | Test âm HTTP có fixture |
| Bảo vệ file/dữ liệu | Link asset/avatar/file, path, size, fail closed | Test F08/F16/F24-F26 |
| Truy vết | Actor-action-resource-outcome, che secret, phân quyền đọc | Audit writer tại app + test |
| Chuỗi cung ứng | npm/Maven/image/secret scan; SBOM nếu cần | Scan đúng SHA/digest và đánh giá reachability |
| Báo cáo | Bằng chứng, mức ảnh hưởng, sửa và regression | Trước/sau có target, không ghi PASS từ kế hoạch |

Chỉ kiểm thử môi trường được quyền; không quét nguồn công cộng hoặc dữ liệu thật. App code fix ở repo app. Không xem ASVS/OWASP tham khảo là chứng nhận đã đạt.
