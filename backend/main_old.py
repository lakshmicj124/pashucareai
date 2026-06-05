"""
PashuCare AI – FastAPI Backend
OpenCV-based livestock disease detection with SQLite storage.
"""

import os
import base64
import uuid
from datetime import datetime
from typing import List

import cv2
import numpy as np
from fastapi import FastAPI, HTTPException, UploadFile, File, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from database import init_db, save_detection, get_user_detections
from models import Disease, Animal, DetectionResult

# ── App setup ────────────────────────────────────────────────────────────────
app = FastAPI(title="PashuCare AI Backend", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads directory
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Serve uploaded images at /uploads/<filename>
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# Initialise database
init_db()

# ── Mock disease catalogue ───────────────────────────────────────────────────
DISEASES = [
    {
        "id": 1,
        "name": "Foot and Mouth Disease",
        "animal": "Cow",
        "confidence": 94,
        "severity": "Critical",
        "severityColor": "red",
        "symptoms": [
            "Fever above 40°C", "Blisters on mouth and hooves",
            "Excessive salivation", "Lameness", "Loss of appetite"
        ],
        "causes": [
            "Picornavirus (FMDV)", "Direct contact with infected animals",
            "Contaminated feed or water", "Airborne transmission"
        ],
        "prevention": [
            "Regular vaccination every 6 months",
            "Quarantine new animals for 14 days",
            "Disinfect farm equipment", "Restrict visitor access"
        ],
        "firstAid": [
            "Isolate the animal immediately",
            "Clean lesions with antiseptic",
            "Provide soft feed and clean water",
            "Call veterinarian urgently",
            "Do not move animals off-farm"
        ],
    },
    {
        "id": 2,
        "name": "Mastitis",
        "animal": "Cow",
        "confidence": 87,
        "severity": "Moderate",
        "severityColor": "amber",
        "symptoms": [
            "Swollen udder", "Hot and painful teats",
            "Abnormal milk (clots/blood)", "Reduced milk production",
            "Mild fever"
        ],
        "causes": [
            "Bacterial infection (Staph, Strep)", "Poor milking hygiene",
            "Teat injuries", "Environmental contamination"
        ],
        "prevention": [
            "Pre and post-dip teats after milking",
            "Maintain clean bedding", "Regular udder health checks",
            "Dry cow therapy"
        ],
        "firstAid": [
            "Strip affected quarters",
            "Apply cold compress to reduce swelling",
            "Ensure clean environment",
            "Consult vet for antibiotics"
        ],
    },
    {
        "id": 3,
        "name": "Lumpy Skin Disease",
        "animal": "Cow",
        "confidence": 91,
        "severity": "Critical",
        "severityColor": "red",
        "symptoms": [
            "Firm, round skin nodules (2-5 cm)",
            "High fever (41°C+)", "Swollen lymph nodes",
            "Reduced milk yield", "Nasal and eye discharge"
        ],
        "causes": [
            "Lumpy Skin Disease Virus (Capripoxvirus)",
            "Spread by mosquitoes and biting flies",
            "Direct contact with infected animals"
        ],
        "prevention": [
            "Annual vaccination with live attenuated vaccine",
            "Insect control (sprays, nets)",
            "Quarantine infected animals immediately",
            "Movement restrictions in outbreak areas"
        ],
        "firstAid": [
            "Isolate affected animal",
            "Apply antiseptic on skin lesions",
            "Provide supportive care (fluids, shade)",
            "Contact veterinarian for treatment protocol"
        ],
    },
    {
        "id": 4,
        "name": "Bloat (Ruminal Tympany)",
        "animal": "Cow",
        "confidence": 82,
        "severity": "Moderate",
        "severityColor": "amber",
        "symptoms": [
            "Distended left abdomen",
            "Difficulty breathing", "Restlessness",
            "Frequent lying down and standing",
            "Stopped chewing cud"
        ],
        "causes": [
            "Excess consumption of legumes or lush pasture",
            "Rapid diet change", "Grain overload",
            "Obstruction of oesophagus"
        ],
        "prevention": [
            "Gradual diet transitions",
            "Mix legumes with grass hay",
            "Provide anti-bloat supplements",
            "Avoid feeding on wet pasture"
        ],
        "firstAid": [
            "Walk the animal to encourage gas release",
            "Use a stomach tube if trained",
            "Administer anti-foaming agent (vegetable oil)",
            "Call vet immediately if severe"
        ],
    },
    {
        "id": 5,
        "name": "Peste des Petits Ruminants (PPR)",
        "animal": "Goat",
        "confidence": 89,
        "severity": "Critical",
        "severityColor": "red",
        "symptoms": [
            "High fever (40-41°C)", "Nasal discharge",
            "Mouth ulcers", "Diarrhea", "Pneumonia"
        ],
        "causes": [
            "PPR virus (Morbillivirus)",
            "Direct contact with infected animals",
            "Contaminated water and feed"
        ],
        "prevention": [
            "Annual PPR vaccination",
            "Quarantine new stock for 21 days",
            "Maintain hygiene in shelters"
        ],
        "firstAid": [
            "Isolate sick animal",
            "Provide oral rehydration solution",
            "Keep warm and sheltered",
            "Contact veterinarian immediately"
        ],
    },
    {
        "id": 6,
        "name": "Foot Rot",
        "animal": "Sheep",
        "confidence": 85,
        "severity": "Moderate",
        "severityColor": "amber",
        "symptoms": [
            "Lameness", "Swelling between toes",
            "Foul-smelling discharge from hooves",
            "Reluctance to walk", "Weight loss"
        ],
        "causes": [
            "Fusobacterium necrophorum bacteria",
            "Wet, muddy conditions",
            "Hoof injuries", "Overcrowding"
        ],
        "prevention": [
            "Regular hoof trimming",
            "Foot baths with zinc sulphate",
            "Well-drained pastures",
            "Vaccinate in endemic areas"
        ],
        "firstAid": [
            "Trim and clean affected hoof",
            "Apply topical antiseptic spray",
            "Move to dry ground",
            "Administer antibiotics if severe"
        ],
    },
]

ANIMALS = [
    {
        "id": "C001", "name": "Lakshmi", "type": "Cow",
        "breed": "Holstein Friesian", "age": 4, "weight": 520,
        "status": "Healthy", "healthScore": 92,
        "lastCheckup": "2025-05-15", "vaccineStatus": "upToDate",
        "image": "🐄",
    },
    {
        "id": "C002", "name": "Nandini", "type": "Cow",
        "breed": "Gir", "age": 6, "weight": 480,
        "status": "Sick", "healthScore": 64,
        "lastCheckup": "2025-05-20", "vaccineStatus": "due",
        "image": "🐄",
    },
    {
        "id": "G001", "name": "Chinnu", "type": "Goat",
        "breed": "Jamunapari", "age": 2, "weight": 45,
        "status": "Healthy", "healthScore": 88,
        "lastCheckup": "2025-05-18", "vaccineStatus": "upToDate",
        "image": "🐐",
    },
    {
        "id": "S001", "name": "Gowri", "type": "Sheep",
        "breed": "Bannur", "age": 3, "weight": 55,
        "status": "Healthy", "healthScore": 90,
        "lastCheckup": "2025-05-10", "vaccineStatus": "upToDate",
        "image": "🐑",
    },
]


# ── OpenCV detection helper ─────────────────────────────────────────────────
def analyse_image(image_bytes: bytes) -> dict:
    """
    Decode the image with OpenCV, run a basic colour-histogram analysis,
    and return the best-matching disease dict from the catalogue.

    For a production app you would replace this with a trained CNN model.
    """
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise HTTPException(status_code=400, detail="Could not decode image")

    # --- Feature extraction (demo-level) ---
    # Convert to HSV and compute a normalised hue histogram
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0], None, [180], [0, 180])
    hist = cv2.normalize(hist, hist).flatten()
    dominant_hue = int(np.argmax(hist))

    # Compute mean BGR for a secondary signal
    mean_b, mean_g, mean_r, _ = cv2.mean(img)

    # --- Naive mapping to an animal type ---
    if 35 < dominant_hue < 85:          # green-ish
        animal_type = "Goat"
    elif dominant_hue < 15 or dominant_hue > 160:  # red-ish
        animal_type = "Cow"
    else:
        animal_type = "Sheep"

    # Filter diseases for this animal type
    matching = [d for d in DISEASES if d["animal"] == animal_type]
    if not matching:
        matching = DISEASES

    # Pick one deterministically based on the hue value
    chosen = matching[dominant_hue % len(matching)]

    # Adjust confidence slightly so each image feels unique
    adj_conf = max(70, min(99, chosen["confidence"] + (dominant_hue % 7) - 3))
    result = dict(chosen)
    result["confidence"] = adj_conf
    return result


# ── Existing endpoints ───────────────────────────────────────────────────────
@app.get("/api/diseases", response_model=List[Disease])
async def get_diseases():
    """Return the full disease catalogue."""
    return DISEASES


@app.get("/api/animals", response_model=List[Animal])
async def get_animals():
    """Return the list of farm animals."""
    return ANIMALS


# ── Detection endpoints ──────────────────────────────────────────────────────
@app.post("/api/detect/upload", response_model=DetectionResult)
async def detect_upload(
    file: UploadFile = File(...),
    user_id: str = Query("demo_user"),
):
    """Accept an uploaded image file, run OpenCV analysis, store result."""
    content = await file.read()
    disease = analyse_image(content)

    # Save image
    ext = os.path.splitext(file.filename or "img.jpg")[1] or ".jpg"
    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(content)

    # Persist to SQLite
    row_id = save_detection(
        user_id=user_id,
        disease_id=disease["id"],
        disease_name=disease["name"],
        confidence=disease["confidence"],
        severity=disease["severity"],
        image_path=filename,
    )

    return DetectionResult(
        id=row_id,
        disease_id=disease["id"],
        disease_name=disease["name"],
        confidence=disease["confidence"],
        severity=disease["severity"],
        severityColor=disease["severityColor"],
        symptoms=disease["symptoms"],
        causes=disease["causes"],
        prevention=disease["prevention"],
        firstAid=disease["firstAid"],
        image_url=f"/uploads/{filename}",
        timestamp=datetime.utcnow().isoformat(),
    )


@app.post("/api/detect/live", response_model=DetectionResult)
async def detect_live(
    payload: dict,
    user_id: str = Query("demo_user"),
):
    """Accept a base64-encoded webcam frame and analyse it."""
    data_uri = payload.get("image", "")
    if not data_uri:
        raise HTTPException(status_code=400, detail="Missing 'image' field")

    # Strip the data URI prefix if present
    if "," in data_uri:
        _, b64_data = data_uri.split(",", 1)
    else:
        b64_data = data_uri

    try:
        image_bytes = base64.b64decode(b64_data)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid base64 data")

    disease = analyse_image(image_bytes)

    filename = f"live_{uuid.uuid4().hex}.jpg"
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(image_bytes)

    row_id = save_detection(
        user_id=user_id,
        disease_id=disease["id"],
        disease_name=disease["name"],
        confidence=disease["confidence"],
        severity=disease["severity"],
        image_path=filename,
    )

    return DetectionResult(
        id=row_id,
        disease_id=disease["id"],
        disease_name=disease["name"],
        confidence=disease["confidence"],
        severity=disease["severity"],
        severityColor=disease["severityColor"],
        symptoms=disease["symptoms"],
        causes=disease["causes"],
        prevention=disease["prevention"],
        firstAid=disease["firstAid"],
        image_url=f"/uploads/{filename}",
        timestamp=datetime.utcnow().isoformat(),
    )


@app.get("/api/detections", response_model=List[DetectionResult])
async def get_detections(user_id: str = Query("demo_user")):
    """Return stored detection history for a user."""
    rows = get_user_detections(user_id)
    results = []
    for row in rows:
        # Enrich with full disease data from catalogue
        disease_data = next(
            (d for d in DISEASES if d["id"] == row["disease_id"]), None
        )
        results.append(DetectionResult(
            id=row["id"],
            disease_id=row["disease_id"],
            disease_name=row["disease_name"],
            confidence=row["confidence"],
            severity=row["severity"],
            severityColor=disease_data["severityColor"] if disease_data else "",
            symptoms=disease_data["symptoms"] if disease_data else [],
            causes=disease_data["causes"] if disease_data else [],
            prevention=disease_data["prevention"] if disease_data else [],
            firstAid=disease_data["firstAid"] if disease_data else [],
            image_url=f"/uploads/{row['image_path']}",
            timestamp=row["timestamp"],
        ))
    return results


# ── Health-check landing page ────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def root():
    return """<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>PashuCare AI API</title>
<style>body{font-family:Inter,sans-serif;display:flex;justify-content:center;
align-items:center;min-height:100vh;background:#0f172a;color:#e2e8f0;margin:0}
.card{text-align:center;padding:3rem;border-radius:1rem;
background:linear-gradient(135deg,rgba(16,185,129,.15),rgba(6,182,212,.15));
border:1px solid rgba(255,255,255,.1);backdrop-filter:blur(12px)}
h1{font-size:2rem;margin-bottom:.5rem}
p{opacity:.7}a{color:#34d399;text-decoration:none}</style></head>
<body><div class="card"><h1>🐄 PashuCare AI API</h1>
<p>Backend is running</p>
<p><a href="/docs">Open API Docs →</a></p></div></body></html>"""
