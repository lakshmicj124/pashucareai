"""Pydantic models for PashuCare AI backend API responses."""

from typing import List
from pydantic import BaseModel


class Disease(BaseModel):
    id: int
    name: str
    animal: str
    confidence: int
    severity: str
    severityColor: str
    symptoms: List[str]
    causes: List[str]
    prevention: List[str]
    firstAid: List[str]


class Animal(BaseModel):
    id: str
    name: str
    type: str
    breed: str
    age: int
    weight: int
    status: str
    healthScore: int
    lastCheckup: str
    vaccineStatus: str
    image: str


class DetectionResult(BaseModel):
    id: int = 0
    disease_id: int
    disease_name: str
    confidence: int
    severity: str
    severityColor: str = ""
    symptoms: List[str] = []
    causes: List[str] = []
    prevention: List[str] = []
    firstAid: List[str] = []
    image_url: str = ""
    timestamp: str = ""
