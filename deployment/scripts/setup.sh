#!/bin/bash
# MedVision AI Setup Script

set -e

echo "🏥 MedVision AI - Setup Script"
echo "================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p data/uploads data/processed data/cache logs models/checkpoints models/configs

# Create .env files from examples
echo "⚙️  Setting up environment variables..."
if [ ! -f backend/.env ]; then
    cp backend/.env.example backend/.env
    echo "✅ Created backend/.env"
fi

if [ ! -f frontend/.env ]; then
    cp frontend/.env.example frontend/.env
    echo "✅ Created frontend/.env"
fi

# Create placeholder files
touch models/checkpoints/.gitkeep
touch data/uploads/.gitkeep
touch data/processed/.gitkeep
touch data/cache/.gitkeep
touch logs/.gitkeep

echo ""
echo "✅ Setup completed successfully!"
echo ""
echo "Next steps:"
echo "1. Update backend/.env with your configuration"
echo "2. Place your model checkpoint in models/checkpoints/"
echo "3. Run: docker-compose up -d"
echo ""
echo "🚀 To start the application:"
echo "   docker-compose up -d"
echo ""
echo "📊 Access points:"
echo "   - Backend API: http://localhost:8000/api/docs"
echo "   - Frontend Dashboard: http://localhost:8501"
echo ""
