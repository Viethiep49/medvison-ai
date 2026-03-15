# BẢN TÓM TẮT DỰ ÁN: MEDVISION AI

**Dự án:** Hệ thống hỗ trợ chẩn đoán X-quang phổi thông minh tích hợp AI  
**Sinh viên thực hiện:** Trương Viết Hiệp  
**Lĩnh vực:** Trí tuệ nhân tạo trong Y tế (HealthTech)

---

## 1. Đặt vấn đề
Hiện nay, các bệnh viện tuyến cơ sở và phòng khám nhỏ thường đối mặt với tình trạng thiếu hụt bác sĩ chẩn đoán hình ảnh chuyên sâu. Việc đọc phim X-quang phổi thủ công không chỉ tốn thời gian mà còn tiềm ẩn rủi ro sai sót do áp lực công việc lớn. Bệnh nhân cũng gặp khó khăn trong việc hiểu rõ các thuật ngữ y khoa phức tạp trên kết quả chẩn đoán.

## 2. Giải pháp MedVision AI
MedVision AI là một hệ thống hỗ trợ chẩn đoán toàn diện, giúp tối ưu hóa quy trình phân tích ảnh X-quang phổi bằng cách kết hợp sức mạnh của thị giác máy tính và ngôn ngữ tự nhiên. 

### Công nghệ cốt lõi:
*   **Mô hình LuX-ViT:** Được phát triển dựa trên kiến trúc Vision Transformer (trong công trình nghiên cứu khoa học của em), chuyên biệt cho việc phát hiện và khoanh vùng 14 loại bệnh lý phổi phổ biến.
*   **Medical LLM:** Một mô hình ngôn ngữ lớn đã được tinh chỉnh (fine-tuned) trên tập dữ liệu y khoa khổng lồ về X-quang phổi, đóng vai trò "trợ lý ảo" giải thích kết quả.

## 3. Quy trình vận hành (Pipeline)
Hệ thống được thiết kế tối giản, dễ dàng triển khai tại các đơn vị y tế nhỏ:
1.  **Tiếp nhận dữ liệu:** Y bác sĩ hoặc bệnh nhân tải ảnh chụp X-quang lên hệ thống sau khi khám.
2.  **Phân tích AI:** Mô hình LuX-ViT tự động nhận diện các dấu hiệu bất thường.
3.  **Trực quan hóa (xAI):** Hệ thống sử dụng các kỹ thuật AI có thể giải thích (Explainable AI) để khoanh vùng tổn thương trực tiếp trên ảnh, giúp bác sĩ dễ dàng đối chiếu.
4.  **Tương tác & Giải thích:** Medical LLM sẽ chuyển đổi các thông số kỹ thuật khô khan thành ngôn ngữ dễ hiểu, đồng thời cho phép người dùng đặt câu hỏi hỏi-đáp trực tiếp về tình trạng bệnh.

## 4. Giá trị mang lại
*   **Đối với Bác sĩ:** Tiết kiệm ~60% thời gian đọc bài; cung cấp ý kiến thứ hai (second opinion) khách quan, tin cậy.
*   **Đối với Bệnh nhân:** Hiểu rõ tình trạng sức khỏe của mình thông qua ngôn ngữ bình dân; giảm bớt lo lắng khi chờ đợi kết quả.
*   **Đối với Cơ sở y tế:** Nâng cao chất lượng dịch vụ chẩn đoán mà không cần đầu tư quá lớn vào hạ tầng nhân sự chuyên trách ban đầu.

## 5. Kết luận
MedVision AI không chỉ dừng lại ở một công cụ phân tích ảnh, mà là một hệ sinh thái hỗ trợ giao tiếp giữa bác sĩ - bệnh nhân và công nghệ, góp phần dân chủ hóa việc tiếp cận dịch vụ chẩn đoán y tế chất lượng cao tại Việt Nam.

---
*Tài liệu đính kèm thư xin phép vắng mặt trình bày dự án ngày 09/03/2026.*
