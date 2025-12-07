"""
Image processing utilities
"""

import numpy as np
from PIL import Image
from typing import Tuple


def resize_image(image: Image.Image, size: Tuple[int, int] = (224, 224)) -> Image.Image:
    """Resize image to target size"""
    return image.resize(size, Image.LANCZOS)


def normalize_image(image: np.ndarray) -> np.ndarray:
    """Normalize image to [0, 1]"""
    return image.astype(np.float32) / 255.0


def draw_bounding_boxes(
    image: Image.Image,
    boxes: list,
    labels: list,
    scores: list
) -> Image.Image:
    """
    Draw bounding boxes on image

    Args:
        image: PIL Image
        boxes: List of bounding boxes [(x1, y1, x2, y2), ...]
        labels: List of labels
        scores: List of confidence scores

    Returns:
        Image with bounding boxes drawn
    """
    # TODO: Implement bounding box drawing
    return image
