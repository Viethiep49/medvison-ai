# MedVision AI - Project Context

## Project Overview

**MedVision AI** is a production-ready MVP for VNPT AI Hackathon 2025, built on the research foundation of LuX-ViT. This is a medical AI application for automated chest X-ray analysis.

### Key Information
- **Purpose**: Hackathon MVP - Production deployment
- **Base Research**: LuX-ViT (in ../lux-vit folder - DO NOT MODIFY)
- **Domain**: Medical imaging - Clinical chest X-ray diagnosis
- **Main Task**: Multi-label disease classification + Bounding box localization
- **Dataset**: ChestX-ray14 (14 pathological conditions)
- **Framework**: FastAPI (backend) + Streamlit (frontend) + PyTorch
- **Author**: Trương Viết Hiệp (HUTECH University)
- **Competition**: VNPT AI Hackathon 2025

### Relationship to LuX-ViT
- **LuX-ViT** (`../lux-vit/`) = Research codebase (KEEP SEPARATE, DO NOT TOUCH)
- **MedVision AI** (this folder) = Production MVP for hackathon
- Model weights will be copied from LuX-ViT after training
- No code sharing between projects - clean separation

## Project Structure

```
medvision-ai/
├── backend/              # FastAPI REST API
│   ├── app/
│   │   ├── api/         # REST endpoints (health, predict, history)
│   │   ├── core/        # Config, logging
│   │   ├── models/      # SQLAlchemy database models
│   │   ├── schemas/     # Pydantic request/response schemas
│   │   └── services/    # Business logic (model inference, image processing)
│   ├── requirements.txt
│   ├── alembic.ini
│   └── .env.example
│
├── frontend/            # Streamlit Dashboard
│   ├── src/
│   │   ├── pages/      # Dashboard pages (home, upload, history, analytics)
│   │   ├── components/ # Reusable UI components
│   │   └── utils/      # API client, image utilities
│   ├── app.py          # Main Streamlit entry point
│   ├── requirements.txt
│   └── .env.example
│
├── models/              # Model artifacts
│   ├── checkpoints/    # .pth model files (copied from LuX-ViT)
│   └── configs/        # Model configuration files
│
├── docker/              # Docker configurations
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── .dockerignore
│
├── deployment/          # Deployment resources
│   ├── scripts/        # setup.sh, start.sh, stop.sh
│   ├── init_db.sql     # Database initialization
│   └── kubernetes/     # K8s configs (future)
│
├── data/               # Runtime data (gitignored)
│   ├── uploads/       # Uploaded X-ray images
│   ├── processed/     # Processed results
│   └── cache/         # Temporary cache
│
├── docs/              # Documentation
│   ├── API.md        # API documentation
│   └── DEPLOYMENT.md # Deployment guide
│
├── logs/              # Application logs (gitignored)
├── tests/             # Unit tests
├── docker-compose.yml # Multi-service orchestration
├── README.md          # Main documentation
└── LICENSE            # MIT License
```

## Tech Stack

### Backend (FastAPI)
- **Framework**: FastAPI 0.104+ (modern, async Python web framework)
- **Server**: Uvicorn (ASGI server)
- **Database**: PostgreSQL 15 (patient records, prediction history)
- **ORM**: SQLAlchemy 2.0
- **Cache**: Redis 7 (fast result caching)
- **Validation**: Pydantic v2
- **ML**: PyTorch 2.0+, Transformers (HuggingFace)

### Frontend (Streamlit)
- **Framework**: Streamlit 1.29+ (interactive dashboard)
- **Visualization**: Plotly, Matplotlib, Seaborn
- **API Client**: Requests, HTTPX
- **Layout**: Multi-page app with navigation

### Infrastructure
- **Containerization**: Docker, Docker Compose
- **Database**: PostgreSQL + Redis
- **Deployment**: Docker-based (cloud-agnostic)

## Code Style & Conventions

### Python Standards
- **Style**: PEP 8
- **Type Hints**: Required for all function signatures
- **Docstrings**: Google-style docstrings for public APIs
- **Formatting**: Black (auto-formatter)
- **Linting**: Flake8
- **Import Sorting**: isort

### Naming Conventions
- **Files**: `snake_case.py`
- **Classes**: `PascalCase` (e.g., `ModelService`, `PredictionResponse`)
- **Functions/Methods**: `snake_case` (e.g., `load_model`, `predict`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_IMAGE_SIZE`)
- **Private**: `_leading_underscore` for internal use

### API Conventions
- **Endpoints**: RESTful, lowercase with hyphens
  - `GET /api/health`
  - `POST /api/predict`
  - `GET /api/history`
- **HTTP Methods**:
  - GET (read), POST (create), PUT (update), DELETE (delete)
- **Response Format**: JSON with consistent structure
- **Error Handling**: HTTP status codes + error messages

### Medical Domain
- **14 Pathologies**: Atelectasis, Cardiomegaly, Effusion, Infiltration, Mass, Nodule, Pneumonia, Pneumothorax, Consolidation, Edema, Emphysema, Fibrosis, Pleural_Thickening, Hernia
- **Image Input**: 224×224 RGB (preprocessed)
- **Output**: Multi-label probabilities (sigmoid) + bounding boxes
- **Threshold**: Configurable (default 0.5)

## Important Files

### Critical Files (Be Careful!)
- `backend/app/main.py` - FastAPI application entry point
- `backend/app/services/model_service.py` - Model inference logic
- `backend/app/core/config.py` - Application configuration
- `frontend/app.py` - Streamlit entry point
- `docker-compose.yml` - Service orchestration

### Configuration Files
- `backend/.env` - Backend environment variables (DATABASE_URL, MODEL_PATH, DEVICE)
- `frontend/.env` - Frontend config (BACKEND_URL)
- `docker-compose.yml` - Service definitions

### Safe to Modify
- Pages in `frontend/src/pages/`
- API endpoints in `backend/app/api/`
- Database models in `backend/app/models/`
- Documentation files

## Development Workflow

### Local Development

1. **Backend**:
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # Edit .env
uvicorn app.main:app --reload
```

2. **Frontend**:
```bash
cd frontend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

3. **Docker (Full Stack)**:
```bash
./deployment/scripts/setup.sh
docker-compose up -d
```

### Testing
```bash
# Run tests
pytest

# With coverage
pytest --cov=app --cov-report=html

# Specific test
pytest tests/test_api.py
```

### Code Quality
```bash
# Format code
black backend/ frontend/

# Sort imports
isort backend/ frontend/

# Lint
flake8 backend/ frontend/
```

## Common Tasks

### Adding a New API Endpoint

1. Create schema in `backend/app/schemas/`
2. Add endpoint in `backend/app/api/`
3. Register router in `backend/app/main.py`
4. Update API documentation in `docs/API.md`
5. Test with `pytest tests/test_api.py`

### Adding a New Dashboard Page

1. Create page in `frontend/src/pages/new_page.py`
2. Implement `render()` function
3. Import in `frontend/app.py`
4. Add to navigation radio buttons
5. Test manually in browser

### Updating Model

1. Train model in `../lux-vit/` (research codebase)
2. Copy checkpoint: `cp ../lux-vit/checkpoints/best.pth models/checkpoints/best_model.pth`
3. Update `backend/.env` MODEL_PATH if needed
4. Restart backend: `docker-compose restart backend`
5. Test prediction: `curl -X POST http://localhost:8000/api/predict -F "file=@test.jpg"`

### Database Migration

```bash
cd backend
# Create migration
alembic revision --autogenerate -m "Description"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Environment Variables

### Backend (.env)
```bash
# Model
MODEL_PATH=../models/checkpoints/best_model.pth
MODEL_TYPE=improved  # base, lora, improved
DEVICE=cuda  # cuda or cpu

# Database
DATABASE_URL=postgresql://medvision:password@localhost:5432/medvision_db

# Redis
REDIS_URL=redis://localhost:6379/0

# API
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8501

# Security
SECRET_KEY=change-this-in-production
```

### Frontend (.env)
```bash
BACKEND_URL=http://localhost:8000
```

## Deployment

### Docker Deployment (Recommended)
```bash
# Setup
./deployment/scripts/setup.sh

# Start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Cloud Deployment
- See `docs/DEPLOYMENT.md` for AWS, Azure, GCP guides
- Kubernetes configs in `deployment/kubernetes/` (TODO)

## API Endpoints

### Health
- `GET /api/health` - Basic health check
- `GET /api/ready` - Model readiness check

### Prediction
- `POST /api/predict` - Single image prediction
- `POST /api/batch-predict` - Batch prediction

### History
- `GET /api/history` - List predictions
- `GET /api/history/{id}` - Get specific prediction
- `DELETE /api/history/{id}` - Delete prediction

See `docs/API.md` for detailed documentation.

## Dashboard Pages

1. **Home** - Welcome, feature highlights, system status
2. **Upload & Analyze** - Upload X-ray, run prediction, view results
3. **History** - View past predictions, filter, search
4. **Analytics** - Statistics, charts, model performance

## Database Schema

### predictions table
- `id` (PK) - Unique prediction ID
- `filename` - Original image filename
- `patient_id` - Optional patient identifier
- `predictions` (JSON) - Disease probabilities
- `bounding_boxes` (JSON) - Localization results
- `model_version` - Model used
- `confidence_score` - Overall confidence
- `processing_time` - Inference time
- `created_at` - Timestamp
- `image_path` - Stored image path

### users table (future)
- For authentication/authorization

## Best Practices

### DO ✅
- Use type hints for all functions
- Add docstrings to public APIs
- Handle errors gracefully with proper HTTP status codes
- Log important events (model loading, predictions, errors)
- Validate input data (file size, type, format)
- Use environment variables for configuration
- Write tests for new features
- Keep secrets out of code (use .env)
- Docker for deployment consistency

### DON'T ❌
- Hardcode paths or credentials
- Commit large model files to git
- Commit patient data or medical images
- Modify `../lux-vit/` research codebase
- Skip input validation
- Expose sensitive data in API responses
- Use synchronous code in async endpoints
- Ignore security best practices

### Security Considerations
- Validate all uploaded files (type, size, content)
- Sanitize file names before storage
- Use HTTPS in production
- Add authentication for production
- Rate limiting on prediction endpoints
- Secure database credentials
- CORS configuration

## Troubleshooting

### Model Not Loading
- Check `models/checkpoints/best_model.pth` exists
- Verify `MODEL_PATH` in `.env`
- Check device (CUDA vs CPU)
- Review logs: `docker-compose logs backend`

### Database Connection Failed
- Check PostgreSQL is running: `docker-compose ps postgres`
- Verify `DATABASE_URL` in `.env`
- Restart database: `docker-compose restart postgres`

### Frontend Can't Connect to Backend
- Check backend is running: `curl http://localhost:8000/api/health`
- Verify `BACKEND_URL` in frontend `.env`
- Check CORS settings in `backend/app/main.py`

### Out of Memory
- Reduce batch size
- Use CPU instead of GPU for inference
- Increase Docker memory limit
- Check for memory leaks

## Performance Optimization

- **Model**: Use quantization, ONNX export, TensorRT
- **Caching**: Redis for frequent predictions
- **Database**: Connection pooling, indexes
- **API**: Async endpoints, background tasks
- **Frontend**: Lazy loading, pagination

## Future Enhancements (Post-Hackathon)

- [ ] User authentication & authorization
- [ ] DICOM file support (pydicom)
- [ ] PDF report generation
- [ ] Email notifications
- [ ] Advanced analytics dashboard
- [ ] Model versioning & A/B testing
- [ ] Kubernetes deployment
- [ ] CI/CD pipeline
- [ ] Monitoring & alerting (Prometheus, Grafana)
- [ ] API rate limiting

## Hackathon Demo Tips

1. **Preparation**:
   - Pre-load model before demo
   - Prepare sample X-ray images
   - Test full workflow end-to-end
   - Have backup plan (screenshots, video)

2. **Demo Flow**:
   - Show dashboard homepage
   - Upload X-ray image
   - Explain AI analysis in real-time
   - Show confidence scores, detected conditions
   - Demonstrate history/analytics
   - Show API documentation (bonus)

3. **Talking Points**:
   - Real-time AI diagnosis
   - 14 pathological conditions
   - High accuracy (95%+)
   - Production-ready architecture
   - Scalable Docker deployment
   - Based on research (LuX-ViT)

## Resources

- **Research Codebase**: `../lux-vit/`
- **API Docs**: http://localhost:8000/api/docs
- **Dashboard**: http://localhost:8501
- **GitHub**: https://github.com/Viethiep49/medvison-ai

## Contact

- **Developer**: Trương Viết Hiệp
- **University**: HUTECH
- **GitHub**: @Viethiep49
- **Competition**: VNPT AI Hackathon 2025

---

**Last Updated**: 2025-12-07
**Project Status**: MVP Development
**Stage**: Pre-Hackathon Setup
