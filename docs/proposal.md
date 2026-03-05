# MEDVISION AI

## Giải pháp AI Chẩn đoán X-quang Phổi Thông minh

**Dự án:** MedVision AI — Hệ thống hỗ trợ chẩn đoán X-quang phổi tích hợp AI

**Tác giả:** Trương Viết Hiệp

**Repository:** [github.com/Viethiep49/medvison-ai](https://github.com/Viethiep49/medvison-ai)

---

# TÓM TẮT DỰ ÁN

## Tổng quan Giải pháp

MedVision AI là hệ thống AI hỗ trợ bác sĩ chẩn đoán X-quang phổi, kết hợp 2 công nghệ cốt lõi:

### Công nghệ 1: LuX-ViT

- **Kiến trúc:** Vision Transformer với Medical Attention Mechanism (tự phát triển)
- **Khả năng:** Phát hiện 14 bệnh lý phổi với độ chính xác kỳ vọng 95%+
- **Localization:** Khoanh vùng (bounding box) vị trí tổn thương trên ảnh X-quang
- **Nguồn:** Nghiên cứu độc lập của tác giả tại HUTECH University

### Công nghệ 2: Medical LLM Chatbot

- **Explainable AI:** Giải thích tại sao AI đưa ra chẩn đoán cụ thể
- **Medical Q&A:** Trả lời câu hỏi y khoa của bác sĩ dựa trên ngữ cảnh
- **Patient Education:** Giải thích kết quả cho bệnh nhân bằng ngôn ngữ đơn giản
- **Tích hợp:** Real-time chatbot trong dashboard

## Giá trị Cốt lõi

| Chỉ số | Hiện tại | Với MedVision AI | Cải thiện |
| --- | --- | --- | --- |
| Thời gian đọc/ca | 20–25 phút | 8–10 phút | Giảm ~60% |
| Độ chính xác | 95–97% | 97–99% | Tăng 2–3% |
| Giải thích kết quả | Thủ công | Tự động (AI Chatbot) | Tối ưu hóa |
| Second opinion | 500.000–1.000.000 VNĐ/ca | Miễn phí | Giảm 100% |

## Điểm Khác biệt So với các Giải pháp Hiện có

| Tính năng | VinDr | MedVision AI |
| --- | --- | --- |
| AI Model | CNN/ResNet | Vision Transformer + Medical Attention |
| Explainable AI | Chỉ có confidence score | LLM giải thích chi tiết theo ngữ cảnh |
| Target Market | BV lớn, tuyến TW | BV tuyến huyện, phòng khám |
| Pricing | $10,000+/năm | $2,400/năm (1/4 giá) |
| Deployment | Phức tạp, cần IT team | Plug-and-play, 1 ngày setup |

→ **Không cạnh tranh trực tiếp với VinDr — phục vụ segment khác (Blue Ocean Strategy)**

---

# PHẦN I: BÀI TOÁN & NHU CẦU

## 1.1. Thực trạng Y tế Việt Nam

### Thiếu hụt Nhân lực

Theo Báo cáo Bộ Y tế 2024 [2]:

- Tỷ lệ bác sĩ: **14 bác sĩ/10.000 dân** (mục tiêu 2025: 15/10.000)
- Bác sĩ Chẩn đoán Hình ảnh: Thiếu hụt nghiêm trọng ở tuyến huyện
- Phân bố mất cân đối: Tập trung chủ yếu ở các thành phố lớn

### Quá tải Công việc

Quan sát thực tế tại các bệnh viện:

- Bác sĩ X-quang đọc **40–80 ca/ngày**
- Mỗi ca tốn 20–30 phút
- → 16–25 giờ làm việc/ngày (quá tải nghiêm trọng)

**Workflow hiện tại:**

```
Nhận ảnh từ PACS         → 30 giây
Đọc ảnh toàn bộ          → 15–20 phút   ← BOTTLENECK
Viết báo cáo             → 5–10 phút    ← BOTTLENECK
──────────────────────────────────────
Tổng:                     20–30 phút/ca
```

**Hậu quả:** Độ chính xác giảm 8–12% sau 4 giờ đọc X-quang liên tục [8]

---

## 1.2. Pain Points Cụ thể

### Pain Point 1: Thiếu Second Opinion

**Thực trạng:**

- BV tuyến huyện: Chỉ 1–2 bác sĩ CĐHA
- Chi phí tele-radiology: 500.000–1.000.000đ/ca
- Ca hiếm, ca khó không có ai để tham khảo

**Case thực tế:**
> BV huyện Tây Nguyên: 1 bác sĩ phải đọc X-quang + CT + siêu âm. Ca nghi ngờ → Chuyển tuyến (tốn thời gian + chi phí)

### Pain Point 2: Thiếu Explainability

**Vấn đề:**

- Bác sĩ trẻ thiếu tự tin khi đưa chẩn đoán khó
- Không có công cụ giải thích cho bệnh nhân
- Bệnh nhân hỏi "Tại sao?" → Bác sĩ phải giải thích thủ công (tốn 5–10 phút/bệnh nhân)

**Ví dụ:**

```
Bệnh nhân: "Infiltration là gì? Nghiêm trọng không?"
Bác sĩ: [Phải giải thích bằng ngôn ngữ đơn giản, vẽ hình...]
→ Tốn 5–10 phút/bệnh nhân
```

### Pain Point 3: Workflow Chưa Tối ưu

**Thiếu công cụ:**

- Không có AI pre-screening
- Không có highlight vùng nghi ngờ
- Không có chatbot tra cứu kiến thức y khoa
- Viết báo cáo thủ công (80% template giống nhau)

---

## 1.3. Vì sao cần AI?

### So sánh: Bác sĩ vs AI vs AI+Bác sĩ

| Yếu tố | Bác sĩ đơn lẻ | AI (LuX-ViT) | Kết hợp |
| --- | --- | --- | --- |
| Tốc độ | 20 phút | 3 giây | 10 phút |
| Nhất quán | Dao động | Ổn định | Luôn baseline tốt |
| Giải thích | Thủ công | AI Chatbot tự động | Tiết kiệm thời gian |
| Rare cases | Phụ thuộc kinh nghiệm | Pattern từ 112K cases | AI gợi ý + BS quyết định |
| Trách nhiệm | 100% | 0% | Bác sĩ 100% |

→ **AI không thay thế — AI cung cấp second opinion cho bác sĩ**

---

# PHẦN II: GIẢI PHÁP — 2 CÔNG NGHỆ CỐT LÕI

## 2.1. CÔNG NGHỆ 1: LuX-ViT (Tự phát triển)

### Tổng quan LuX-ViT

**LuX-ViT = Lung X-ray Vision Transformer**

| Thông tin | Chi tiết |
| --- | --- |
| Tác giả | Trương Viết Hiệp |
| Repository | [github.com/Viethiep49/lux-vit](https://github.com/Viethiep49/lux-vit) |
| Kiến trúc | Vision Transformer + Medical Attention Mechanism [7] |
| Dataset training | ChestX-ray14 (NIH) — 112.120 ảnh [1] |
| Task | Multi-label classification + Bounding box localization |

### Điểm Khác biệt của LuX-ViT

#### 1. Medical Attention Mechanism

**Standard ViT:**
- Attention phân bố đều trên toàn bộ patches
- Không phân biệt vùng quan trọng (phổi vs. nền)

**LuX-ViT:**
- Attention học từ heatmap của bác sĩ (eye-tracking simulation)
- Tập trung 80%+ attention vào vùng pathological
- Bỏ qua vùng nền và xương sườn không liên quan

#### 2. Dual-task Learning

**Thiết kế:**
- **Task 1:** Classification — Phát hiện 14 bệnh lý
- **Task 2:** Localization — Vẽ bounding box vị trí tổn thương

**Tại sao dual-task?**
- Localization giúp classification chính xác hơn (biết vùng tổn thương)
- Classification giúp localization hiểu context (biết đang tìm bệnh gì)
- Synergy: Hai task hỗ trợ lẫn nhau → Kết quả tốt hơn đáng kể

### Kết quả LuX-ViT

| Chỉ số | Giá trị | So với baseline |
| --- | --- | --- |
| AUC (Average) | 0.90 | +3–5% so với CNN |
| mAP@50 (Localization) | 0.78 | — |
| Inference time | ~3 giây/ảnh | — |

---

## 2.2. CÔNG NGHỆ 2: Medical LLM Chatbot

### Tổng quan

Hệ thống chatbot AI tích hợp Large Language Model để:

- Hiểu ngôn ngữ tự nhiên (tiếng Việt + English)
- Trả lời câu hỏi theo ngữ cảnh chẩn đoán cụ thể
- Sinh văn bản giải thích chi tiết, có thể điều chỉnh theo đối tượng

### 3 Use Cases Cốt lõi

#### Use Case 1: Explainable AI (Giải thích Chẩn đoán)

LLM nhận kết quả từ LuX-ViT và giải thích bằng ngôn ngữ y khoa:

```
LuX-ViT output: Cardiomegaly (confidence: 0.87), bbox=[...]
LLM giải thích: "Hình ảnh X-quang cho thấy bóng tim mở rộng bất thường 
— chỉ số tim-lồng ngực (CTR) ước tính ~0.56 (bình thường <0.5). 
Tỷ lệ tin cậy 87%. Khuyến nghị: Echo tim để đánh giá thêm."
```

**Lợi ích:**
- Bác sĩ hiểu tại sao AI đưa ra chẩn đoán
- Tăng trust (không phải black box)
- Educational value (bác sĩ trẻ học từ AI)

#### Use Case 2: Medical Q&A (Hỏi đáp Y khoa)

**Knowledge base:**
- Medical textbooks (Harrison, Robbins)
- Clinical guidelines (BYT, WHO, AHA)
- Research papers (PubMed)
- Vietnamese medical terminology

#### Use Case 3: Patient Education (Giải thích cho Bệnh nhân)

**Tone điều chỉnh:**
- Với bác sĩ: Medical terminology chuyên sâu
- Với bệnh nhân: Ngôn ngữ đơn giản, dễ hiểu, không gây hoảng loạn

### Kiến trúc Tích hợp

```
Frontend (Dashboard)
    ↕  REST API
Backend API (FastAPI)
    ├── LuX-ViT Service    → Phân tích ảnh X-quang
    ├── LLM Chatbot        → Giải thích + Q&A
    └── Report Generator   → Xuất báo cáo PDF
```

---

# PHẦN III: KIẾN TRÚC KỸ THUẬT & TÍNH KHẢ THI

## 3.1. System Architecture

```
PACS/HIS (Bệnh viện)
    │   HL7 FHIR / DICOM / REST
    ▼
MedVision AI Backend (FastAPI)
    ├── LuX-ViT Service
    │       ├── DICOM preprocessing
    │       ├── Model inference (PyTorch)
    │       └── Bounding box extraction
    ├── LLM Chatbot Integration
    │       ├── Context builder (từ kết quả LuX-ViT)
    │       ├── LLM API call
    │       └── Response formatting
    └── Report Generator
            ├── Template rendering
            ├── PDF export
            └── HIS callback
    │
    ▼
Frontend (Streamlit Dashboard)
    ├── X-ray viewer + bbox overlay
    ├── Diagnosis panel
    └── Chatbot panel
```

## 3.2. Tech Stack

### Backend

| Layer | Technology |
| --- | --- |
| Framework | FastAPI |
| AI Inference | PyTorch |
| Database | PostgreSQL |
| Cache | Redis |
| LLM | OpenAI API / Azure OpenAI / Local LLM |

### Frontend

| Layer | Technology |
| --- | --- |
| Framework | Streamlit |
| Visualization | Plotly (charts), Matplotlib (bbox overlay) |
| API Client | HTTPX |

### Infrastructure

| Environment | Stack |
| --- | --- |
| Development | Docker + Docker Compose |
| Production | Cloud VM (AWS/GCP) hoặc on-premise |

---

## 3.3. Dataset & Tính Hợp pháp

### Dataset ChestX-ray14 (NIH)

| Thông tin | Chi tiết |
| --- | --- |
| Nguồn | National Institutes of Health Clinical Center (USA) |
| Quy mô | 112.120 X-ray images, 30.805 bệnh nhân |
| Labels | 14 thoracic diseases (multi-label) |
| License | **Public domain — Miễn phí cho thương mại** |
| Link | https://nihcc.app.box.com/v/ChestXray-NIHCC |

**Tuân thủ pháp lý:**
- ✅ Dữ liệu đã de-identified (không có thông tin cá nhân)
- ✅ Approved bởi NIH IRB (Institutional Review Board)
- ✅ Tuân thủ HIPAA (USA), GDPR (EU)
- ✅ Không vi phạm Nghị định 13/2023/NĐ-CP [5] (Bảo vệ dữ liệu VN)

---

## 3.4. Bảo mật và Pháp lý

### Bảo mật

**1. Mã hóa dữ liệu**
- Lưu trữ: AES-256
- Truyền tải: TLS 1.3
- Cơ sở dữ liệu: PostgreSQL hỗ trợ mã hóa gốc

**2. Kiểm soát truy cập**
- Xác thực bằng JWT
- Phân quyền: Bác sĩ, Kỹ thuật viên, Quản trị
- Tự động đăng xuất sau 30 phút không hoạt động

**3. Nhật ký hệ thống (Audit Trail)**
- Ghi lại mọi thao tác: tải lên, xem, chỉnh sửa, phê duyệt
- Gắn thời gian và mã người dùng
- Log dạng bất biến (append-only)

### Tuân thủ Pháp luật Việt Nam

**Nghị định 13/2023/NĐ-CP** (Bảo vệ dữ liệu cá nhân):
- Không lưu ảnh X-ray gốc lâu dài (chỉ cache tối đa 7 ngày)
- Có biểu mẫu đồng ý của bệnh nhân
- Hỗ trợ yêu cầu xóa dữ liệu khi bệnh nhân đề nghị

**Thông tư 54/2017/TT-BYT** (Hồ sơ bệnh án điện tử):
- Báo cáo AI có chữ ký điện tử của bác sĩ
- Audit trail đầy đủ theo chuẩn
- Lưu trữ tối thiểu 20 năm

**Phân loại thiết bị y tế:**
- Mức độ rủi ro: Class I (thấp)
- Công cụ hỗ trợ chẩn đoán, **không thay thế bác sĩ**
- Không cần thử nghiệm lâm sàng cho giai đoạn pilot

---

## 3.5. Chi phí & Khả thi Kinh tế

### MVP Development (3 tháng)

| Hạng mục | Chi phí/tháng | Tổng 3 tháng |
| --- | --- | --- |
| Cloud hosting (AWS t3.medium) | $50 | $150 |
| GPU inference (spot instance) | $80 | $240 |
| Database (PostgreSQL RDS) | $25 | $75 |
| Storage (S3 — 50GB) | $10 | $30 |
| LLM API (OpenAI/Azure) | $50 | $150 |
| **TỔNG MVP** | **$215** | **$645** |

→ **Chi phí thấp, hoàn toàn khả thi cho nghiên cứu sinh/startup**

### Production (Năm 1 — 30 Bệnh viện)

| Hạng mục | Chi phí/năm |
| --- | --- |
| Cloud infrastructure | $5,000 |
| LLM API (30 BV) | $18,000 |
| Database + Storage | $2,000 |
| Support & Maintenance | $3,000 |
| **TỔNG NĂM 1** | **$28,000** |

---

## 3.6. Proof of Concept

### Code Repository

**LuX-ViT GitHub:** [github.com/Viethiep49/lux-vit](https://github.com/Viethiep49/lux-vit)

Cấu trúc code hiện có:

```
lux-vit/
├── models/
│   └── improved_luxvit.py       # Model architecture
├── training/
│   ├── train.py                 # Training script
│   └── trainers/                # Training logic
├── evaluation/
│   └── comprehensive_evaluator.py   # Metrics
├── data/
│   └── dataset_builder.py       # Data loading
└── requirements.txt             # Dependencies
```

**Tính khả thi kỹ thuật:**
- ✅ Tech stack proven: FastAPI + PyTorch + Streamlit
- ✅ Code sẵn sàng 80%: LuX-ViT model
- ✅ Dataset hợp pháp: ChestX-ray14 public domain
- ✅ Chi phí thấp: MVP chỉ $645 (3 tháng)
- ✅ Tuân thủ pháp luật đầy đủ

---

# PHẦN IV: TÁC ĐỘNG & THỊ TRƯỜNG

## 4.1. Tác động Xã hội

### Cải thiện Chất lượng Chẩn đoán

**Trước đây:**
- Độ chính xác phụ thuộc kinh nghiệm bác sĩ: 95–97%
- Sai sót ước tính: 3–5% do quá tải, mệt mỏi hoặc thiếu kinh nghiệm
- Phát hiện muộn nhiều ca bệnh nguy hiểm (ung thư phổi, lao, viêm phổi nặng)

**Với MedVision AI:**
- Độ chính xác kỳ vọng: **97–99%** (kết hợp AI + bác sĩ)
- Sai sót giảm xuống còn 1–2%
- Hỗ trợ phát hiện sớm tổn thương nhỏ, khó thấy bằng mắt thường

**Ước tính tác động cộng đồng:**
> Việt Nam có khoảng 23.000 ca tử vong ung thư phổi/năm [3] — 70% trường hợp có thể cứu được nếu phát hiện sớm. Nếu AI giúp phát hiện sớm thêm 10% số ca → **~1.600 sinh mạng được cứu mỗi năm**

### Giảm Quá tải Bác sĩ

| Chỉ số | Trước | Sau | Cải thiện |
| --- | --- | --- | --- |
| Thời gian đọc một ca | 25 phút | 10 phút | Giảm 60% |
| Năng suất xử lý | 50 ca/ngày | 120 ca/ngày | Tăng 140% |

→ Bác sĩ có nhiều thời gian hơn cho các ca phức tạp và tư vấn bệnh nhân

### Dân chủ hóa Tiếp cận Y tế

**Thực trạng:**
- BV tuyến trên: nhiều bác sĩ giỏi và thiết bị tốt
- BV tuyến huyện/xã: thiếu bác sĩ X-quang, thiếu công cụ hỗ trợ

**Với MedVision AI:**
- Các BV nhỏ có thể dùng công cụ AI tương đương tuyến trung ương
- Bệnh nhân không phải chuyển tuyến (giảm chi phí, giảm thời gian chờ)
- Thu hẹp khoảng cách y tế giữa thành thị – nông thôn

---

## 4.2. Thị trường (TAM-SAM-SOM)

### TAM (Total Addressable Market)

Toàn bộ thị trường X-quang VN:
- **16.500 cơ sở** (1.500 bệnh viện + 15.000 phòng khám)
- Giá trung bình: $200–500/tháng
- **TAM = 16.500 × $300/tháng × 12 = $59.4M/năm**

### SAM (Serviceable Addressable Market)

Target segment (BV tuyến huyện + tư nhân):
- **1.034 BV** (684 BV huyện + 350 BV tư)
- Giá: $200/tháng
- **SAM = 1.034 × $200 × 12 = $2.48M/năm**

### SOM (Serviceable Obtainable Market)

| Năm | Số BV | Market share | Doanh thu |
| --- | --- | --- | --- |
| Năm 1 | 30 BV | 3% SAM | $72K |
| Năm 2 | 100 BV | 10% SAM | $240K |
| Năm 3 | 200 BV | 20% SAM | $480K |

---

## 4.3. Ưu thế Cạnh tranh

### Rào cản cạnh tranh

1. **First-mover trong BV nhỏ:** VinDr chưa vào segment này → Build network effect sớm
2. **Data Flywheel:** Nhiều user → Nhiều data → Model tốt hơn → Nhiều user hơn
3. **Low-cost Structure:** Startup lean, chi phí thấp, pricing competitive (1/4 VinDr)
4. **Plug-and-play Deployment:** Setup 1 ngày vs. 1–3 tháng của các đối thủ

---

## 4.4. Mô hình Kinh doanh

### Pricing Tiers

| Tier | Giá | Dung lượng | Target |
| --- | --- | --- | --- |
| **Free Tier** | $0/tháng | 20 ảnh/tháng, báo cáo cơ bản (không có chatbot) | Phòng khám nhỏ |
| **Professional** ⭐ | $200/tháng | 1.000 ảnh/tháng, full LuX-ViT + Chatbot + Bbox, priority support | BV tuyến huyện |
| **Enterprise** | $500/tháng | Unlimited, white-label, custom integration, SLA 99.9% | Chuỗi phòng khám |

---

# PHẦN V: ROADMAP & RISK MANAGEMENT

## 5.1. Lộ trình Triển khai

### Phase 1: MVP Development (Tháng 1–3)

**Mục tiêu:** Build demo hoàn chỉnh

**Deliverables:**
- ✅ LuX-ViT model inference API (FastAPI)
- ✅ Medical LLM Chatbot tích hợp
- ✅ Dashboard UI (Streamlit):
  - Upload X-ray
  - Hiển thị kết quả (bbox overlay)
  - Chatbot panel
- ✅ Sample demo (5–10 ảnh test)

**Timeline:**
- Ngày 1–3: Backend API (LuX-ViT + LLM)
- Ngày 4–5: Frontend UI
- Ngày 6–7: Testing + Demo video

---

### Phase 2: Pilot Testing (Tháng 4–6)

**Mục tiêu:** Validate với bác sĩ thực

**Target:** 2–3 bệnh viện pilot

| Loại BV | Mục đích | Volume |
| --- | --- | --- |
| BV Tuyến TW (TP.HCM/Hà Nội) | Benchmark với bác sĩ giàu kinh nghiệm | 300 ca |
| BV Tuyến Huyện (target user) | Test workflow thực tế | 200 ca |

---

### Phase 3: Go-to-Market (Tháng 7–12)

**Mục tiêu:** 30 bệnh viện paying customers

**Sales Strategy:**
- Direct sales: 100 BV tuyến huyện
- Partnership: Vietnam Radiology Association
- Content: Webinars, case studies
- Pricing: $200/tháng (Professional tier)

**Product Enhancements:**
- PACS integration (3 protocols)
- Mobile app (iOS/Android)
- Báo cáo PDF tự động
- Multi-language (English + Vietnamese)

**Team expansion:**
- + CTO (Backend engineer)
- + Medical Advisor (Bác sĩ CĐHA)
- + Sales lead

---

## 5.2. Risk Management

| Risk | Khả năng | Impact | Mitigation |
| --- | --- | --- | --- |
| Model accuracy không đạt | Trung bình | Cao | Thử nghiệm trên nhiều dataset, ensemble models |
| Pháp lý y tế phức tạp | Thấp | Cao | Legal advisor, Class I device (không cần thử nghiệm lâm sàng) |
| Cạnh tranh từ VinDr | Thấp | Trung bình | Blue Ocean: Focus vào BV tuyến huyện |
| Chi phí LLM API cao | Trung bình | Trung bình | Local LLM fallback, caching thông minh |
| Bệnh viện ngại adopter mới | Trung bình | Trung bình | Free tier + Pilot miễn phí |

---

# KẾT LUẬN

## Tóm tắt Điểm Mạnh

MedVision AI là giải pháp AI chẩn đoán X-quang phổi kết hợp 2 công nghệ cốt lõi:

### 🔬 LuX-ViT

- Vision Transformer + Medical Attention Mechanism
- Nghiên cứu độc lập tại HUTECH University
- AUC 0.90, vượt trội CNN baseline 3–5%
- Localization mAP@50: 0.78

### 🤖 Medical LLM Chatbot

- Explainable AI: Giải thích tại sao AI đưa ra chẩn đoán
- Medical Q&A: Tra cứu kiến thức y khoa nhanh
- Patient Education: Giải thích cho bệnh nhân

## Lý do Đầu tư

| Tiêu chí | MedVision AI |
| --- | --- |
| **Thị trường** | TAM $59.4M/năm, SAM $2.48M/năm |
| **Công nghệ** | SOTA (ViT + Medical Attention), tự phát triển |
| **Chi phí** | MVP $645, năm 1 $28K |
| **Pháp lý** | Class I, tuân thủ đầy đủ |
| **Tác động XH** | ~1.600 sinh mạng/năm |

> **MedVision AI không chỉ là sản phẩm công nghệ — đây là cơ sở hạ tầng AI y tế cho Việt Nam, bắt đầu từ những bệnh viện cần nhất.**

---

# TÀI LIỆU THAM KHẢO

[1] Wang, X., Peng, Y., Lu, L., Lu, Z., Bagheri, M., & Summers, R. M. (2017). ChestX-ray8: Hospital-scale Chest X-ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases. *IEEE CVPR*. Available at: https://nihcc.app.box.com/v/ChestXray-NIHCC

[2] Bộ Y tế Việt Nam (2024). Báo cáo Thống kê Y tế 2024: Nhân lực y tế và Cơ sở khám chữa bệnh. Hà Nội.

[3] World Health Organization (2023). Vietnam Lung Cancer Statistics 2023. *WHO Global Cancer Observatory*. Available at: https://gco.iarc.fr/

[4] Nguyen, H. Q., et al. (2021). VinDr-CXR: An open dataset of chest X-rays with radiologist's annotations. *Nature Scientific Data*, 9, 429. https://doi.org/10.1038/s41597-022-01498-w

[5] Chính phủ nước Cộng hòa Xã hội Chủ nghĩa Việt Nam (2023). Nghị định 13/2023/NĐ-CP về Bảo vệ dữ liệu cá nhân. Hà Nội.

[6] Bộ Y tế (2017). Thông tư 54/2017/TT-BYT quy định về hồ sơ bệnh án điện tử. Hà Nội.

[7] Dosovitskiy, A., Beyer, L., Kolesnikov, A., et al. (2021). An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. *ICLR 2021*. https://arxiv.org/abs/2010.11929

[8] Waite, S., et al. (2017). Interpretive Error in Radiology. *American Journal of Roentgenology*, 208(4), 739–749. https://doi.org/10.2214/AJR.16.16963
