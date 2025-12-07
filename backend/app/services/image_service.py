"""
Image processing service
"""

import io
import numpy as np
from PIL import Image
from fastapi import UploadFile, HTTPException
from app.core.config import settings
from app.core.logging import logger


class ImageService:
    """Service for image validation and preprocessing"""

    @staticmethod
    async def validate_and_load(file: UploadFile) -> np.ndarray:
        """
        Validate and load image file

        Args:
            file: Uploaded image file

        Returns:
            Preprocessed image array

        Raises:
            ValueError: If image is invalid
        """
        # Check file extension
        file_ext = file.filename.split('.')[-1].lower()
        if f".{file_ext}" not in settings.ALLOWED_EXTENSIONS:
            raise ValueError(
                f"Invalid file type. Allowed: {settings.ALLOWED_EXTENSIONS}"
            )

        # Check file size
        contents = await file.read()
        if len(contents) > settings.MAX_IMAGE_SIZE:
            raise ValueError(
                f"File too large. Max size: {settings.MAX_IMAGE_SIZE / 1024 / 1024}MB"
            )

        try:
            # Load image
            image = Image.open(io.BytesIO(contents))

            # Convert to RGB
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Resize
            image = image.resize(
                (settings.IMAGE_SIZE, settings.IMAGE_SIZE),
                Image.LANCZOS
            )

            # Convert to array
            image_array = np.array(image)

            logger.info(f"Image loaded: {file.filename}, shape: {image_array.shape}")

            return image_array

        except Exception as e:
            logger.error(f"Failed to process image: {e}")
            raise ValueError(f"Failed to process image: {e}")

    @staticmethod
    def preprocess(image: np.ndarray) -> np.ndarray:
        """
        Preprocess image for model input

        Args:
            image: Image array

        Returns:
            Preprocessed image
        """
        # Normalize to [0, 1]
        image = image.astype(np.float32) / 255.0

        # TODO: Add ImageNet normalization if needed
        # mean = [0.485, 0.456, 0.406]
        # std = [0.229, 0.224, 0.225]

        return image
