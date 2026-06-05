"""Pydantic models for disease detection results."""

from typing import List
from pydantic import BaseModel


class DetectionResult(BaseModel):
    id: str = ""
    disease_name: str = ""
    animal_type: str = ""
    confidence: float = 0.0
    severity: str = ""
    severity_color: str = ""
    symptoms: List[str] = []
    causes: List[str] = []
    why_it_happened: str = ""
    prevention: List[str] = []
    medicine: List[str] = []
    first_aid: List[str] = []
    food_recommendations: List[str] = []
    hygiene_tips: List[str] = []
    image_url: str = ""
    timestamp: str = ""
    user_id: str = ""
    emergency: str = ""
    top_3_predictions: list = []
    top_predictions: list = []
    animal: str = ""
    disease: str = ""


