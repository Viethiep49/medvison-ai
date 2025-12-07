#!/bin/bash
# Stop MedVision AI services

echo "🛑 Stopping MedVision AI..."

docker-compose down

echo "✅ Services stopped!"
