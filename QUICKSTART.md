# 🚀 MedVision AI - Quick Start Guide

## Bắt Đầu Nhanh (Vietnamese)

### Yêu Cầu
- Docker & Docker Compose
- Model checkpoint từ LuX-ViT (đã train xong)

### Các Bước Setup (5 phút)

#### 1. Clone & Setup
```bash
cd /Users/kaito/Documents/lung\ model/medvision-ai
chmod +x deployment/scripts/*.sh
./deployment/scripts/setup.sh
```

#### 2. Copy Model từ LuX-ViT
```bash
# Copy model đã train từ LuX-ViT
cp ../lux-vit/checkpoints/best_model.pth models/checkpoints/best_model.pth

# Hoặc nếu file khác tên:
# cp ../lux-vit/path/to/model.pth models/checkpoints/best_model.pth
```

#### 3. Cấu Hình (Tùy Chọn)
```bash
# Chỉnh backend/.env nếu cần
nano backend/.env

# Quan trọng: Kiểm tra
# - MODEL_PATH=../models/checkpoints/best_model.pth
# - DEVICE=cuda (nếu có GPU) hoặc cpu
```

#### 4. Khởi Động
```bash
# Khởi động tất cả services
docker-compose up -d

# Xem logs
docker-compose logs -f
```

#### 5. Truy Cập
- **Dashboard**: http://localhost:8501
- **API Docs**: http://localhost:8000/api/docs
- **Health Check**: http://localhost:8000/api/health

### Kiểm Tra Hoạt Động

```bash
# Test API
curl http://localhost:8000/api/health

# Test prediction (nếu có ảnh test)
curl -X POST "http://localhost:8000/api/predict" \
  -F "file=@test_xray.jpg"
```

### Dừng Services
```bash
docker-compose down
```

---

## Development Mode (Không dùng Docker)

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
# → http://localhost:8000
```

### Frontend
```bash
cd frontend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
# → http://localhost:8501
```

### Database (Riêng)
```bash
# Chỉ chạy PostgreSQL
docker-compose up -d postgres redis

# Hoặc cài local PostgreSQL và tạo DB
createdb medvision_db
psql medvision_db < deployment/init_db.sql
```

---

## Chuẩn Bị Demo Hackathon

### Checklist Demo
- [ ] Model checkpoint đã có trong `models/checkpoints/`
- [ ] Services chạy OK: `docker-compose ps`
- [ ] Test upload ảnh X-ray qua dashboard
- [ ] Chuẩn bị 3-5 ảnh X-ray mẫu để demo
- [ ] Test full flow: Upload → Analyze → View Results
- [ ] Kiểm tra History và Analytics pages
- [ ] Screenshot hoặc record màn hình (backup plan)

### Demo Flow
1. Mở dashboard: http://localhost:8501
2. Giới thiệu tổng quan (Home page)
3. Upload X-ray → Upload & Analyze
4. Giải thích kết quả (diseases, confidence, bounding boxes)
5. Show History (các prediction trước)
6. Show Analytics (statistics, charts)
7. Bonus: Show API docs nếu có thời gian

### Backup Plan (Nếu Live Demo Fail)
- Screenshots của các bước
- Video recording
- Prepared slides với kết quả

---

## Troubleshooting

### Lỗi: Model not found
```bash
# Kiểm tra model file
ls -lh models/checkpoints/

# Nếu chưa có, copy từ LuX-ViT
cp ../lux-vit/checkpoints/*.pth models/checkpoints/best_model.pth
```

### Lỗi: Port already in use
```bash
# Tìm và kill process
sudo lsof -ti:8000 | xargs kill -9  # Backend
sudo lsof -ti:8501 | xargs kill -9  # Frontend
```

### Lỗi: Docker out of memory
```bash
# Tăng memory limit trong Docker Desktop Settings
# Hoặc chạy local (không dùng Docker)
```

### Lỗi: CUDA out of memory
```bash
# Chuyển sang CPU mode
# Edit backend/.env
DEVICE=cpu
docker-compose restart backend
```

### Services không start
```bash
# Xem logs chi tiết
docker-compose logs backend
docker-compose logs frontend
docker-compose logs postgres

# Restart specific service
docker-compose restart backend
```

---

## Cấu Trúc Project (Tham Khảo)

```
medvision-ai/
├── backend/              # FastAPI API
├── frontend/             # Streamlit Dashboard
├── models/               # Model checkpoints
├── docker/               # Docker configs
├── deployment/           # Scripts
├── docs/                 # Documentation
└── data/                 # Runtime data
```

### Files Quan Trọng
- `README.md` - Tài liệu chính
- `docker-compose.yml` - Service orchestration
- `backend/app/main.py` - Backend entry
- `frontend/app.py` - Frontend entry
- `.claude/CLAUDE.md` - Project context (cho AI)

---

## Next Steps

### Sau Khi Setup Xong

1. **Test Local**
   - Upload vài ảnh X-ray
   - Kiểm tra predictions
   - Xem history

2. **Customize (Optional)**
   - Thêm logo: `frontend/public/logo.png`
   - Chỉnh màu sắc dashboard
   - Thêm thông tin team

3. **Prepare Demo**
   - Chuẩn bị presentation slides
   - Test full demo flow 2-3 lần
   - Chuẩn bị Q&A

4. **Documentation**
   - Đọc `docs/API.md`
   - Đọc `docs/DEPLOYMENT.md`
   - Review `.claude/CLAUDE.md` (AI context)

---

## Resources

- **GitHub**: https://github.com/Viethiep49/medvison-ai
- **Research**: ../lux-vit/ (research codebase)
- **API Docs**: http://localhost:8000/api/docs
- **Dashboard**: http://localhost:8501

---

## Support

Nếu gặp vấn đề:
1. Kiểm tra logs: `docker-compose logs -f`
2. Review `.claude/CLAUDE.md` (có troubleshooting section)
3. Check GitHub Issues
4. Review LuX-ViT research code (nếu về model)

---

**Good luck với VNPT AI Hackathon! 🏥🚀**
