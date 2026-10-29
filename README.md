# WorkSphere Security - An toàn thông tin

Repo chuyên đề kiểm chứng an toàn cho [worksphere-app](https://github.com/Khiemnh158/worksphere-app). Không có bản backend riêng; mọi fix sản phẩm nằm ở app.

**Hiện trạng: có audit và probe local đã chạy; chưa có bộ test bảo mật toàn diện, SAST/Maven/image scan hoặc kết quả khắc phục mọi lỗi.** Target nguồn chuẩn tại [target.json](target.json), app commit `dfea1d9b6fc0abdc764d311dbefbcccbf8b9cadd`.

## Đã đưa vào
- [Phạm vi môn](docs/COURSE_SCOPE.md), [TODO](TODO.md), [trạng thái](STATUS.md).
- [34 phát hiện nguồn gốc](findings/baseline-findings.json) và [kết quả HTTP đã che dữ liệu](evidence/baseline/runtime-probes.json).
- Kết quả npm audit baseline để phân loại; không tự nhận mọi cảnh báo đã vá.
- `tests/baseline/auth_probe.py`: probe đã dùng local. Đọc hướng dẫn trước, chỉ chạy với tài khoản thử riêng và môi trường được quyền.

## Môn này phải làm tiếp
Threat model/DFD, ma trận quyền, regression test âm có fixture, xác thực/session, file/input, audit, secret/SCA và báo cáo trước/sau cùng target commit. Hai patch F01/F02 đã nhập ở app; F03/F04 vẫn mở. SCA Maven/image chưa chạy. Đề cương môn chưa có, đây là phương án đề xuất cần đối chiếu giảng viên.

Repo liên quan: [app](https://github.com/Khiemnh158/worksphere-app) • [deployment](https://github.com/Khiemnh158/worksphere-deployment). Không đưa token, mật khẩu, DB dump hay log nhạy cảm vào evidence.
