"""Disease detection routes — upload image, get results, view history."""

import os
import uuid
from datetime import datetime, timezone
from typing import List

from fastapi import APIRouter, HTTPException, UploadFile, File, Form, Depends, Query
from bson import ObjectId

from ..models.detection import DetectionResult
from ..services.ai_service import detect_disease, get_all_diseases
from ..middleware.auth import get_current_user
from ..database import get_db
from ..config import settings

router = APIRouter(prefix="/api", tags=["Detection"])



@router.post("/detect", response_model=DetectionResult)
async def detect_upload(
    file: UploadFile = File(...),
    animal_type: str = Form("Cow"),
    lang: str = Form("en"),
    user=Depends(get_current_user),
):
    """Accept an uploaded image, run AI analysis, store and return result."""
    from ..services.translation_service import get_validation_message
    # Accept if content type starts with image/ or if file has a known image extension
    filename_lower = file.filename.lower()
    valid_exts = (".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif", ".bmp")
    is_image_mime = file.content_type.startswith("image/")
    is_valid_ext = filename_lower.endswith(valid_exts)
    
    if not (is_image_mime or is_valid_ext):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")

    content = await file.read()
    if len(content) > 10 * 1024 * 1024:  # 10MB limit
        raise HTTPException(status_code=400, detail=get_validation_message("file_too_large", lang))

    if len(content) == 0:
        raise HTTPException(status_code=400, detail=get_validation_message("empty_file", lang))

    # 1. Run Animal Classification validation
    from ..services.ai_service import classify_animal
    detected_animal = classify_animal(content, file.filename, animal_type)
    
    if detected_animal != animal_type:
        if detected_animal in ["Cow", "Goat", "Sheep"]:
            raise HTTPException(
                status_code=400,
                detail=get_validation_message("invalid_animal", lang, detected=detected_animal, expected=animal_type.lower())
            )
        else:
            raise HTTPException(
                status_code=400,
                detail=get_validation_message("animal_not_found", lang, expected=animal_type.lower())
            )

    # 2. Run AI detection
    disease = detect_disease(content, animal_type, file.filename)
    if "error" in disease:
        raise HTTPException(status_code=400, detail=disease["error"])

    # Save uploaded image
    ext = os.path.splitext(file.filename)[1] or ".jpg"
    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(settings.UPLOAD_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(content)

    now = datetime.now(timezone.utc).isoformat()
    user_id = str(user.get("_id", "anonymous"))

    # Build result
    result = DetectionResult(
        disease_name=disease["name"],
        animal_type=disease["animal"],
        confidence=disease["confidence"],
        severity=disease["severity"],
        severity_color=disease["severity_color"],
        symptoms=disease["symptoms"],
        causes=disease["causes"],
        why_it_happened=disease["why_it_happened"],
        prevention=disease["prevention"],
        medicine=disease["medicine"],
        first_aid=disease["first_aid"],
        food_recommendations=disease["food_recommendations"],
        hygiene_tips=disease["hygiene_tips"],
        image_url=f"/uploads/{filename}",
        timestamp=now,
        user_id=user_id,
        emergency="",
    )

    # Save to database
    db = get_db()
    if db is not None:
        doc = result.model_dump()
        insert_result = await db.detections.insert_one(doc)
        result.id = str(insert_result.inserted_id)

    # Translate result to requested language for response
    from ..services.translation_service import translate_disease_data
    translated_dict = translate_disease_data(result.model_dump(), lang)
    translated_dict["id"] = result.id
    
    return DetectionResult(**translated_dict)


@router.get("/detections", response_model=List[DetectionResult])
async def get_detections(
    lang: str = Query("en"),
    user=Depends(get_current_user)
):
    """Return detection history for the current user, translated to requested language."""
    db = get_db()
    if db is None:
        return []

    user_id = str(user.get("_id", "anonymous"))
    cursor = db.detections.find({"user_id": user_id}).sort("timestamp", -1).limit(50)
    results = []
    from ..services.translation_service import translate_disease_data
    async for doc in cursor:
        doc["id"] = str(doc.pop("_id"))
        translated_doc = translate_disease_data(doc, lang)
        # Ensure emergency field is present
        if "emergency" not in translated_doc:
            translated_doc["emergency"] = ""
        results.append(DetectionResult(**translated_doc))
    return results


@router.get("/diseases")
async def get_diseases(lang: str = Query("en")):
    """Return the complete disease catalogue, translated to requested language."""
    diseases = get_all_diseases()
    from ..services.translation_service import translate_disease_data
    return [translate_disease_data(d, lang) for d in diseases]


@router.delete("/detections/{detection_id}")
async def delete_detection(detection_id: str, user=Depends(get_current_user)):
    """Delete a specific detection record from history."""
    db = get_db()
    if db is None:
        raise HTTPException(status_code=503, detail="Database not available.")

    user_id = str(user.get("_id", "anonymous"))
    try:
        oid = ObjectId(detection_id)
        result = await db.detections.delete_one({"_id": oid, "user_id": user_id})
    except Exception:
        # Fallback for string keys (Mock DB / string ids)
        result = await db.detections.delete_one({"id": detection_id, "user_id": user_id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Detection record not found or not owned by user.")

    return {"success": True, "message": "Detection history entry deleted successfully."}
