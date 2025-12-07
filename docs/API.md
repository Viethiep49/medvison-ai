# MedVision AI - API Documentation

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, the API does not require authentication. This will be added in future versions.

## Endpoints

### Health Check

#### `GET /api/health`

Check if the API is running.

**Response:**
```json
{
  "status": "healthy",
  "service": "MedVision AI",
  "version": "0.1.0"
}
```

#### `GET /api/ready`

Check if the model is loaded and ready.

**Response:**
```json
{
  "status": "ready",
  "model_loaded": true,
  "device": "cuda"
}
```

### Prediction

#### `POST /api/predict`

Analyze a chest X-ray image.

**Request:**
- Content-Type: `multipart/form-data`
- Body:
  - `file`: Image file (JPG, PNG, DICOM)
  - `threshold` (optional): Detection threshold (0.0-1.0, default: 0.5)
  - `patient_id` (optional): Patient identifier

**Response:**
```json
{
  "prediction_id": "uuid-string",
  "filename": "chest_xray.jpg",
  "diseases": [
    {
      "disease": "Pneumonia",
      "probability": 0.85,
      "threshold": 0.5,
      "positive": true
    },
    {
      "disease": "Cardiomegaly",
      "probability": 0.65,
      "threshold": 0.5,
      "positive": true
    }
  ],
  "bounding_boxes": [
    {
      "x_min": 100,
      "y_min": 150,
      "x_max": 200,
      "y_max": 250,
      "confidence": 0.85,
      "label": "Pneumonia"
    }
  ],
  "model_version": "improved",
  "confidence_score": 0.85,
  "processing_time": 2.3,
  "timestamp": "2025-12-07T10:30:00Z",
  "detected_conditions": ["Pneumonia", "Cardiomegaly"],
  "risk_level": "high"
}
```

**Error Responses:**

- `400 Bad Request`: Invalid file type or size
- `500 Internal Server Error`: Prediction failed

#### `POST /api/batch-predict`

Analyze multiple chest X-ray images.

**Request:**
- Content-Type: `multipart/form-data`
- Body:
  - `files`: Array of image files

**Response:**
```json
{
  "predictions": [
    {
      "filename": "xray1.jpg",
      "result": { /* prediction response */ }
    },
    {
      "filename": "xray2.jpg",
      "result": { /* prediction response */ }
    }
  ]
}
```

### History

#### `GET /api/history`

Get prediction history.

**Query Parameters:**
- `limit` (optional): Number of records (default: 100)
- `offset` (optional): Offset for pagination (default: 0)

**Response:**
```json
[
  {
    "prediction_id": "uuid-string",
    "filename": "chest_xray.jpg",
    "patient_id": "P001",
    "predictions": {
      "Pneumonia": 0.85,
      "Cardiomegaly": 0.65
    },
    "detected_conditions": ["Pneumonia", "Cardiomegaly"],
    "model_version": "improved",
    "confidence_score": 0.85,
    "processing_time": 2.3,
    "created_at": "2025-12-07T10:30:00Z"
  }
]
```

#### `GET /api/history/{prediction_id}`

Get specific prediction by ID.

**Response:**
Same as single item in history list.

#### `DELETE /api/history/{prediction_id}`

Delete prediction record.

**Response:**
```json
{
  "message": "Prediction deleted successfully"
}
```

## Error Codes

- `200`: Success
- `400`: Bad Request (invalid input)
- `404`: Not Found
- `500`: Internal Server Error

## Rate Limiting

Not currently implemented. Will be added in production.

## Examples

### cURL Examples

```bash
# Health check
curl http://localhost:8000/api/health

# Predict
curl -X POST "http://localhost:8000/api/predict" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@chest_xray.jpg" \
  -F "threshold=0.5"

# Get history
curl http://localhost:8000/api/history?limit=10
```

### Python Examples

```python
import requests

# Health check
response = requests.get("http://localhost:8000/api/health")
print(response.json())

# Predict
with open("chest_xray.jpg", "rb") as f:
    response = requests.post(
        "http://localhost:8000/api/predict",
        files={"file": f},
        params={"threshold": 0.5}
    )
print(response.json())

# Get history
response = requests.get(
    "http://localhost:8000/api/history",
    params={"limit": 10}
)
print(response.json())
```

## Interactive Documentation

Visit http://localhost:8000/api/docs for interactive Swagger UI documentation.
