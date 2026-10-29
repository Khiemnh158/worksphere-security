# Probe baseline local

auth_probe.py là phép thử đã dùng trong audit, được đổi cấu hình sang biến môi trường để chia sẻ source không chứa credentials. Không phải toàn bộ security test suite và chưa chạy lại script portable sau khi tách.

- Yêu cầu Python 3 + backend local đang chạy, tài khoản thử ACTIVE riêng.
- Cấp WORKSPHERE_TEST_BASE_URL (mặc định http://127.0.0.1:18080/api/v1), WORKSPHERE_TEST_LOGIN và WORKSPHERE_TEST_PASSWORD trong phiên terminal riêng; không ghi giá trị thật vào Git.
- Từ root security: `python tests/baseline/auth_probe.py`.
- Script tạo phiên riêng, logout phiên đó, thử lại access token, chạy 2 refresh đồng thời và thu hồi refresh token sinh ra. Có ghi dữ liệu session/audit trong DB thử; không chạy trên production.
- Kết quả mới: work/runtime-probes.json (ignored); baseline đã chạy nằm ở evidence/baseline.
- Script chỉ nhận localhost để tránh vô tình kiểm thử hệ thống khác; không tự bỏ chặn này chỉ để chạy trên public.
