# Lộ trình & Tiến độ MedVision AI

Đây là tài liệu ghi nhận tiến độ triển khai kỹ thuật, các quyết định kiến trúc và checklist công việc hàng tuần cho dự án MedVision AI.

## 1. Thiết kế Database Schema (MVP)

Dựa trên quá trình Brainstorming, database được thiết kế theo hướng Relational, linh hoạt mở rộng, và tối ưu cho quy trình hiện tại (Upload X-ray -> AI Scan -> Chatbot -> Doctor Notes).

**Công nghệ:** PostgreSQL
**ORM dự kiến:** SQLAlchemy (FastAPI)

### 1.1 Bảng `scans` (Ca chụp X-quang)
Bảng trung tâm lưu trữ thông tin bệnh nhân và trạng thái xử lý ảnh.
- `id` (UUID, Primary Key): ID định danh duy nhất của ca chụp.
- `patient_name` (Varchar, nullable): Tên bệnh nhân.
- `patient_age` (Integer, nullable): Tuổi.
- `patient_gender` (Varchar, nullable): Giới tính.
- `image_path` (Varchar, not null): Đường dẫn lưu trữ ảnh X-quang gốc (Local/S3).
- `status` (Varchar, not null): Trạng thái xử lý của AI (vd: `processing`, `completed`, `failed`).
- `doctor_notes` (Text, nullable): Ghi chú, chẩn đoán cuối cùng của bác sĩ.
- `created_at` (Timestamp, mặc định now()): Thời gian tạo.
- `updated_at` (Timestamp): Thời gian cập nhật gần nhất.

### 1.2 Bảng `scan_findings` (Kết quả phân tích từ LuX-ViT)
Lưu kết quả bệnh lý do mô hình AI phát hiện. Liên kết 1-nhiều với bảng `scans`.
- `id` (UUID, Primary Key): ID định danh của finding.
- `scan_id` (UUID, Foreign Key): Trỏ đến `scans.id`.
- `disease_name` (Varchar, not null): Tên bệnh lý được phát hiện (vd: "Cardiomegaly", "Pneumonia").
- `confidence_score` (Float, not null): Độ tin cậy của mô hình (0.0 đến 1.0).
- `bounding_box` (JSONB, nullable): Tọa độ khoanh vùng tổn thương (vd: `{"x": 100, "y": 200, "w": 50, "h": 70}`).
- `created_at` (Timestamp, mặc định now()).

### 1.3 Bảng `chat_messages` (Lịch sử Chatbot LLM)
Lưu trữ nội dung trò chuyện giữa bác sĩ và Medical LLM liên quan đến một ca chụp cụ thể.
- `id` (UUID, Primary Key): ID tin nhắn.
- `scan_id` (UUID, Foreign Key): Trỏ đến `scans.id`.
- `role` (Varchar, not null): Vai trò người gửi (vd: `user`, `assistant`, `system`).
- `content` (Text, not null): Nội dung tin nhắn (Câu hỏi của bác sĩ hoặc giải thích của LLM).
- `created_at` (Timestamp, mặc định now()).

---

## 2. Nhật ký Quyết định (Decision Log)
- **2026-03-15:** Thống nhất bỏ qua hệ thống User/Auth cho MVP để tập trung vào tính năng cốt lõi (Phân tích X-quang & Chatbot).
- **2026-03-15:** Gộp thông tin Patient cơ bản vào bảng `scans` thay vì tạo bảng `patients` riêng để tăng tốc độ phát triển. Có thể di chuyển dữ liệu sau này.
- **2026-03-15:** Chọn cấu trúc Database dạng Relational (`scan_findings`) thay vì Flat Table để dễ dàng mở rộng khi LuX-ViT hỗ trợ nhận diện nhiều bệnh hơn trong tương lai.
- **2026-03-15:** Bổ sung trường `doctor_notes` vào bảng `scans` để bác sĩ có thể ghi nhận ý kiến chẩn đoán cuối cùng.

---

## 3. Checklist Tuần này (Tuần 1 MVP)

- [ ] Khởi tạo dự án FastAPI (Cấu trúc thư mục).
- [ ] Thiết lập kết nối PostgreSQL và tích hợp Alembic cho Database Migrations.
- [ ] Định nghĩa các SQLAlchemy Models (Tạo 3 bảng trên).
- [ ] Tạo API Endpoints cơ bản (Upload ảnh, Lấy thông tin ca chụp).
- [ ] (Tùy chọn) Viết script mock data để có dữ liệu test thử cho Frontend.

(Tài liệu này sẽ được cập nhật liên tục trong quá trình phát triển).
