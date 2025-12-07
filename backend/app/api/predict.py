"""
Prediction endpoints
"""

from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import Dict
from app.services.model_service import ModelService
from app.services.image_service import ImageService
from app.schemas.prediction import PredictionResponse

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
async def predict_xray(file: UploadFile = File(...)):
    """
    Analyze chest X-ray image

    Args:
        file: X-ray image file (JPG, PNG, DICOM)

    Returns:
        Prediction results with disease probabilities and bounding boxes
    """
    try:
        # Validate and process image
        image = await ImageService.validate_and_load(file)

        # Run inference
        result = await ModelService.predict(image)

        return result

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


@router.post("/batch-predict")
async def batch_predict(files: list[UploadFile] = File(...)):
    """
    Batch prediction for multiple X-ray images
    """
    results = []

    for file in files:
        try:
            image = await ImageService.validate_and_load(file)
            result = await ModelService.predict(image)
            results.append({"filename": file.filename, "result": result})
        except Exception as e:
            results.append({"filename": file.filename, "error": str(e)})

    return {"predictions": results}
