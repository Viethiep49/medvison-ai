# Deployment Guide

## Docker Deployment (Recommended)

### Prerequisites
- Docker 20.10+
- Docker Compose 1.29+

### Steps

1. **Setup environment**
```bash
./deployment/scripts/setup.sh
```

2. **Configure settings**
```bash
# Edit backend/.env
nano backend/.env

# Update these settings:
# - DATABASE_URL
# - DEVICE (cuda/cpu)
# - MODEL_PATH
```

3. **Start services**
```bash
docker-compose up -d
```

4. **Verify deployment**
```bash
# Check services
docker-compose ps

# Check logs
docker-compose logs -f

# Health check
curl http://localhost:8000/api/health
```

### Service URLs
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/api/docs

## Cloud Deployment

### AWS Deployment

#### Using EC2

1. **Launch EC2 instance**
   - Instance type: t3.medium (minimum), g4dn.xlarge (with GPU)
   - OS: Ubuntu 22.04 LTS
   - Storage: 50GB+

2. **Install Docker**
```bash
sudo apt update
sudo apt install docker.io docker-compose -y
sudo usermod -aG docker ubuntu
```

3. **Deploy application**
```bash
git clone https://github.com/Viethiep49/medvison-ai.git
cd medvision-ai
./deployment/scripts/setup.sh
docker-compose up -d
```

4. **Configure security group**
   - Allow inbound: 8000 (API), 8501 (Frontend)
   - Allow outbound: All

#### Using ECS (Elastic Container Service)

See `deployment/aws/ecs-task-definition.json` for configuration.

### Azure Deployment

#### Using Azure Container Instances

```bash
# Login to Azure
az login

# Create resource group
az group create --name medvision-rg --location eastus

# Create container instances
az container create \
  --resource-group medvision-rg \
  --name medvision-backend \
  --image your-registry/medvision-backend:latest \
  --dns-name-label medvision-api \
  --ports 8000

az container create \
  --resource-group medvision-rg \
  --name medvision-frontend \
  --image your-registry/medvision-frontend:latest \
  --dns-name-label medvision-app \
  --ports 8501
```

### GCP Deployment

#### Using Cloud Run

```bash
# Build and push images
gcloud builds submit --tag gcr.io/PROJECT_ID/medvision-backend backend/
gcloud builds submit --tag gcr.io/PROJECT_ID/medvision-frontend frontend/

# Deploy backend
gcloud run deploy medvision-backend \
  --image gcr.io/PROJECT_ID/medvision-backend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated

# Deploy frontend
gcloud run deploy medvision-frontend \
  --image gcr.io/PROJECT_ID/medvision-frontend \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## Production Considerations

### Security
- Enable HTTPS/SSL
- Add authentication
- Use secrets management
- Configure CORS properly
- Regular security updates

### Performance
- Use GPU instances for faster inference
- Enable Redis caching
- Configure CDN for static files
- Database connection pooling

### Monitoring
- Setup logging (CloudWatch/Stackdriver)
- Configure alerts
- Monitor resource usage
- Track API metrics

### Backup
- Regular database backups
- Model checkpoint backups
- Configuration backups

## Troubleshooting

### Common Issues

**Port already in use**
```bash
# Kill process on port
sudo lsof -ti:8000 | xargs kill -9
```

**Out of memory**
```bash
# Increase Docker memory limit
# Edit Docker Desktop settings or docker-compose.yml
```

**Model not loading**
```bash
# Check model file exists
ls -lh models/checkpoints/

# Check logs
docker-compose logs backend
```

**Database connection failed**
```bash
# Check database is running
docker-compose ps postgres

# Restart database
docker-compose restart postgres
```
