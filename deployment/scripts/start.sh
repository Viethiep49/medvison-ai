#!/bin/bash
# Start MedVision AI services

echo "🚀 Starting MedVision AI..."

# Start services
docker-compose up -d

echo "✅ Services started!"
echo ""
echo "📊 Access points:"
echo "   - Backend API: http://localhost:8000/api/docs"
echo "   - Frontend Dashboard: http://localhost:8501"
echo "   - Health Check: http://localhost:8000/api/health"
echo ""
echo "📝 View logs:"
echo "   docker-compose logs -f"
echo ""
