# Baseline 29/10/2026

Đã tái hiện logout vẫn dùng được access token và refresh race hai HTTP 200. Có kết quả npm audit high 1/low 4 package entries. Các phép thử này chạy trước lượt tách repo trên bản app cùng source + hai patch local. Chưa chạy lại trên clone mới; chưa sửa F03/F04.

Hai patch F01/F02 nằm ở app; baseline-findings.json giữ trạng thái tại thời điểm audit gốc để truy vết. Không có scan Sonar/SAST/Maven/image hay pentest public được xác nhận.
