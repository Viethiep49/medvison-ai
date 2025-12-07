"""
API client for backend communication
"""

import requests
from typing import Dict, Any, Optional


class APIClient:
    """Client for MedVision AI backend API"""

    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()

    def health_check(self) -> Dict[str, Any]:
        """Check API health"""
        response = self.session.get(f"{self.base_url}/api/health")
        response.raise_for_status()
        return response.json()

    def predict(
        self,
        image_file,
        threshold: float = 0.5,
        patient_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send image for prediction

        Args:
            image_file: Image file object
            threshold: Detection threshold
            patient_id: Optional patient ID

        Returns:
            Prediction results
        """
        files = {"file": image_file}
        params = {"threshold": threshold}

        if patient_id:
            params["patient_id"] = patient_id

        response = self.session.post(
            f"{self.base_url}/api/predict",
            files=files,
            params=params
        )
        response.raise_for_status()
        return response.json()

    def get_history(
        self,
        limit: int = 100,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get prediction history"""
        params = {"limit": limit, "offset": offset}
        response = self.session.get(
            f"{self.base_url}/api/history",
            params=params
        )
        response.raise_for_status()
        return response.json()

    def get_prediction(self, prediction_id: str) -> Dict[str, Any]:
        """Get specific prediction by ID"""
        response = self.session.get(
            f"{self.base_url}/api/history/{prediction_id}"
        )
        response.raise_for_status()
        return response.json()
