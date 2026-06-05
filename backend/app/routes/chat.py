import os
import uuid
import httpx
from typing import List, Optional
from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, Depends, UploadFile, File, Form
from pydantic import BaseModel

from ..config import settings
from ..middleware.auth import get_current_user
from ..database import get_db

router = APIRouter(prefix="/api", tags=["Chat"])



class Message(BaseModel):
    role: str  # "user" or "model" (or "assistant")
    text: str


class ChatRequest(BaseModel):
    messages: Optional[List[Message]] = None
    message: Optional[str] = None
    session_id: Optional[str] = None
    lang: Optional[str] = "en"


def get_local_fallback_response(messages: List[Message], lang: str = "en") -> str:
    """Provide high-quality local rule-based veterinary responses if Gemini fails."""
    last_msg = messages[-1].text if messages else ""
    user_text = last_msg.lower().strip()
    
    # 1. Greetings
    if any(g in user_text for g in ["hello", "hi", "hey", "namaste", "help"]):
        if lang == "hi":
            return "नमस्ते! मैं आपका पशुकेयर एआई सहायक हूँ। आज मैं पशु स्वास्थ्य, बीमारी के लक्षणों या प्रबंधन में आपकी क्या मदद कर सकता हूँ?"
        elif lang == "kn":
            return "ನಮಸ್ಕಾರ! ನಾನು ನಿಮ್ಮ ಪಶುಕೇರ್ ಎಐ ಸಹಾಯಕ. ಇಂದು ನಾನು ಜಾನುವಾರುಗಳ ಆರೋಗ್ಯ ಅಥವಾ ನಿರ್ವಹಣೆಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು?"
        else:
            return "Hello! I am your PashuCare AI Assistant. How can I help you with livestock health, animal diseases, symptoms, prevention, or farm management today?"

    # 2. Off-Topic
    off_topic_keywords = ["code", "programming", "python", "javascript", "movie", "politics", "sports", "cricket"]
    if any(ot in user_text for ot in off_topic_keywords):
        if lang == "hi":
            return "मैं केवल पशु स्वास्थ्य और पशुपालन से संबंधित प्रश्नों के उत्तर देने में सक्षम हूँ।"
        elif lang == "kn":
            return "ನಾನು ಪ್ರಾಣಿಗಳ ಆರೋಗ್ಯ ಮತ್ತು ಜಾನುವಾರು ಆರೈಕೆಗೆ ಸಂಬಂಧಿಸಿದ ಪ್ರಶ್ನೆಗಳಿಗೆ ಮಾತ್ರ ಉತ್ತರಿಸಬಲ್ಲೆ."
        else:
            return "I am only programmed to assist with animal health, livestock diseases, symptoms, prevention, recommended feed, and farm management."

    # 3. Feed & Nutrition
    if any(k in user_text for k in ["feed", "food", "diet", "nutrition", "चारा"]):
        if lang == "hi":
            return "पशुओं के संतुलित आहार में हरा चारा, सूखा चारा और साफ पानी शामिल होना चाहिए। खनिज मिश्रण भी दें।"
        elif lang == "kn":
            return "ಜಾನುವಾರುಗಳ ಸಮತೋಲನ ಆಹಾರದಲ್ಲಿ ಹಸಿರು ಮೇವು, ಒಣ ಮೇವು ಮತ್ತು ಶುದ್ಧ ನೀರು ಇರಬೇಕು."
        else:
            return "A balanced diet for livestock includes high-quality green fodder, dry roughage, and clean water. Add concentrate grain mixes and mineral supplements."

    # 4. Shed & Hygiene
    if any(k in user_text for k in ["hygiene", "shed", "clean", "manure"]):
        if lang == "hi":
            return "पशु शेड को साफ, सूखा और हवादार रखें। रोजाना गोबर हटाएँ।"
        elif lang == "kn":
            return "ಕೊಟ್ಟಿಗೆಯನ್ನು ಸ್ವಚ್ಛವಾಗಿ, ಒಣದಾಗಿ ಮತ್ತು ಗಾಳಿಯಾಡುವಂತೆ ಇರಿಸಿ."
        else:
            return "Keep the animal shed clean, dry, and well-ventilated. Regularly clean the floors and remove manure daily."

    # 5. Vaccination
    if any(k in user_text for k in ["vaccine", "vaccination", "schedule", "लसीकरण", "ಲಸಿಕೆ"]):
        if lang == "hi":
            return "गायों के लिए एफएमडी और लम्पी त्वचा रोग का टीका लगवाएं। बकरियों के लिए पीपीआर टीका लगवाएं।"
        elif lang == "kn":
            return "ಹಸುಗಳಿಗೆ ಎಫ್ಎಂಡಿ ಮತ್ತು ಲಂಪಿ ಚರ್ಮ ರೋಗಕ್ಕೆ ಲಸಿಕೆ ಹಾಕಿ. ಆಡುಗಳಿಗೆ ಪಿಪಿಆರ್ ಲಸಿಕೆ ನೀಡಿ."
        else:
            return "Timely vaccination is key to disease prevention. Vaccinate cows against FMD and Lumpy Skin Disease. Vaccinate goats/sheep against PPR."

    # Default
    if lang == "hi":
        return "मुझे समझ में आया कि आप पशु स्वास्थ्य के बारे में पूछ रहे हैं। कृपया अधिक जानकारी दें जैसे पशु प्रकार (गाय, बकरी, भेड़) और लक्षण।"
    elif lang == "kn":
        return "ಜಾನುವಾರು ಆರೋಗ್ಯದ ಬಗ್ಗೆ ನೀವು ಕೇಳುತ್ತಿದ್ದೀರಿ ಎಂದು ನನಗೆ ತಿಳಿದಿದೆ. ದಯವಿಟ್ಟು ಪ್ರಾಣಿಯ ಪ್ರಕಾರ ಮತ್ತು ರೋಗಲಕ್ಷಣಗಳನ್ನು ತಿಳಿಸಿ."
    else:
        return "I understand you are asking about livestock health. To provide the best guidance, please mention the animal type (Cow, Goat, Sheep) and the specific symptoms you observe, or ask about a specific disease like Mastitis, Lumpy Skin, PPR, or Bloat."


@router.get("/chat/sessions")
async def get_sessions(user=Depends(get_current_user)):
    """Fetch all chat sessions for the current logged-in user."""
    from ..services.chat_service import get_user_sessions
    user_id = str(user.get("_id") or user.get("id"))
    sessions = await get_user_sessions(user_id)
    return sessions


@router.get("/chat/sessions/{session_id}/messages")
async def get_messages(session_id: str, user=Depends(get_current_user)):
    """Retrieve all messages for a specific session."""
    db = get_db()
    user_id = str(user.get("_id") or user.get("id"))
    
    # Verify owner
    session = await db.chat_sessions.find_one({"_id": session_id, "user_id": user_id})
    if not session:
        session = await db.chat_sessions.find_one({"id": session_id, "user_id": user_id})
        if not session:
            raise HTTPException(status_code=404, detail="Chat session not found")
            
    from ..services.chat_service import get_session_messages
    messages = await get_session_messages(session_id)
    return messages


@router.delete("/chat/sessions/{session_id}")
async def delete_chat_session(session_id: str, user=Depends(get_current_user)):
    """Delete a chat session and its messages."""
    user_id = str(user.get("_id") or user.get("id"))
    from ..services.chat_service import delete_session
    success = await delete_session(session_id, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="Chat session not found or not owned by user")
    return {"success": True, "message": "Session deleted successfully"}


@router.post("/chat")
async def chat_with_ai(request: ChatRequest, user=Depends(get_current_user)):
    """Interact with Gemini 1.5 Flash using database-backed session history and translations."""
    user_id = str(user.get("_id") or user.get("id"))
    session_id = request.session_id
    lang = request.lang or "en"
    
    from ..services.chat_service import create_session, generate_response, add_message
    
    # If session_id and single message is provided
    if session_id or request.message:
        if not session_id:
            title_text = request.message or "New Chat"
            session = await create_session(user_id, title_text)
            session_id = session["id"]
            
        message_text = request.message or ""
        response_text = await generate_response(session_id, user_id, message_text, lang)
        return {
            "response": response_text,
            "session_id": session_id
        }
    elif request.messages:
        # Fallback for legacy calls from the front-end (sends whole history)
        # Create a new session to store the conversation
        session = await create_session(user_id, "New Chat")
        session_id = session["id"]
        
        # Save previous context messages
        for msg in request.messages[:-1]:
            role = "user" if msg.role not in ("assistant", "model") else "assistant"
            await add_message(session_id, user_id, role, msg.text, lang)
            
        # Generate response for current query
        message_text = request.messages[-1].text
        response_text = await generate_response(session_id, user_id, message_text, lang)
        return {
            "response": response_text,
            "session_id": session_id
        }
    else:
        raise HTTPException(
            status_code=400, 
            detail="Either a 'session_id' and 'message' or a list of 'messages' must be provided."
        )


@router.post("/chat/image")
async def chat_with_image(
    file: UploadFile = File(...),
    animal_type: str = Form("Cow"),
    lang: str = Form("en"),
    session_id: Optional[str] = Form(None),
    user=Depends(get_current_user)
):
    """Run full animal classification & disease diagnostics on image, returning a chat-formatted response."""
    from ..services.ai_service import classify_animal, detect_disease
    from ..services.translation_service import get_validation_message, translate_disease_data
    from ..models.detection import DetectionResult
    
    # 1. Accept if content type starts with image/ or if file has a known image extension
    filename_lower = file.filename.lower()
    valid_exts = (".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif", ".bmp")
    is_image_mime = file.content_type.startswith("image/")
    is_valid_ext = filename_lower.endswith(valid_exts)
    
    if not (is_image_mime or is_valid_ext):
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Please upload an image."
        )

    content = await file.read()
    if len(content) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail=get_validation_message("file_too_large", lang))
    if len(content) == 0:
        raise HTTPException(status_code=400, detail=get_validation_message("empty_file", lang))

    # 2. Run Animal Classification validation
    detected_animal = classify_animal(content, file.filename, animal_type)
    if detected_animal != animal_type:
        if detected_animal in ["Cow", "Goat", "Sheep"]:
            raise HTTPException(
                status_code=400,
                detail=get_validation_message(
                    "invalid_animal", lang, detected=detected_animal, expected=animal_type.lower()
                )
            )
        else:
            raise HTTPException(
                status_code=400,
                detail=get_validation_message("animal_not_found", lang, expected=animal_type.lower())
            )

    # 3. Run AI detection
    disease = detect_disease(content, animal_type, file.filename)
    if "error" in disease:
        raise HTTPException(status_code=400, detail=disease["error"])

    # 4. Save uploaded image
    import os
    _, ext = os.path.splitext(file.filename)
    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(settings.UPLOAD_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(content)

    now = datetime.now(timezone.utc).isoformat()
    user_id = str(user.get("_id", "anonymous"))

    # 5. Build Result Model
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

    # 6. Save in database (detection collection)
    db = get_db()
    if db is not None:
        doc = result.model_dump()
        insert_result = await db.detections.insert_one(doc)
        result.id = str(insert_result.inserted_id)

    # 7. Translate
    translated_dict = translate_disease_data(result.model_dump(), lang)

    # Format fields into a beautiful user-friendly AI chat response
    symptoms_str = "\n".join([f"- {s}" for s in translated_dict.get("symptoms", [])])
    first_aid_str = "\n".join([f"- {f}" for f in translated_dict.get("first_aid", [])])
    medicine_str = "\n".join([f"- {m}" for m in translated_dict.get("medicine", [])])

    if disease['name'] == "Healthy":
        if lang == "hi":
            response_text = f"कोई बीमारी नहीं पाई गई। {translated_dict.get('animal_type')} स्वस्थ प्रतीत होता है।"
        elif lang == "kn":
            response_text = f"ಯಾವುದೇ ರೋಗ ಪತ್ತೆಯಾಗಿಲ್ಲ. {translated_dict.get('animal_type')} ಆರೋಗ್ಯಕರವಾಗಿ ಕಾಣಿಸುತ್ತಿದೆ."
        else:
            response_text = f"No disease detected. {translated_dict.get('animal_type')} appears healthy."
    else:
        if lang == "hi":
            response_text = (
                f"मैंने आपकी छवि का विश्लेषण किया है। ऐसा लगता है कि आपके {translated_dict.get('animal_type')} को **{translated_dict.get('disease_name')}** है (विश्वास स्तर: {translated_dict.get('confidence')}%).\n\n"
                f"**गंभीरता:** {translated_dict.get('severity')}\n\n"
                f"**लक्षण:**\n{symptoms_str}\n\n"
                f"**प्राथमिक उपचार:**\n{first_aid_str}\n\n"
                f"**सुझाई गई दवाएं:**\n{medicine_str}"
            )
        elif lang == "kn":
            response_text = (
                f"ನಾನು ನಿಮ್ಮ ಚಿತ್ರವನ್ನು ವಿಶ್ಲೇಷಿಸಿದ್ದೇನೆ. ನಿಮ್ಮ {translated_dict.get('animal_type')} ಗೆ **{translated_dict.get('disease_name')}** ಇದೆ ಎಂದು ತೋರುತ್ತಿದೆ (ವಿಶ್ವಾಸಾರ್ಹತೆ ಮಟ್ಟ: {translated_dict.get('confidence')}%).\n\n"
                f"**ತೀವ್ರತೆ:** {translated_dict.get('severity')}\n\n"
                f"**ರೋಗಲಕ್ಷಣಗಳು:**\n{symptoms_str}\n\n"
                f"**ಪ್ರಥಮ ಚಿಕಿತ್ಸೆ:**\n{first_aid_str}\n\n"
                f"**ಸೂಚಿಸಲಾದ ಔಷಧಗಳು:**\n{medicine_str}"
            )
        else:
            response_text = (
                f"I have analyzed your image. It looks like your {translated_dict.get('animal_type')} has **{translated_dict.get('disease_name')}** (Confidence level: {translated_dict.get('confidence')}%).\n\n"
                f"**Severity:** {translated_dict.get('severity')}\n\n"
                f"**Symptoms:**\n{symptoms_str}\n\n"
                f"**First Aid:**\n{first_aid_str}\n\n"
                f"**Suggested Medicine:**\n{medicine_str}"
            )

    # 8. Handle chat session persistence for image diagnostics
    if not session_id:
        from ..services.chat_service import create_session
        session_title = f"{translated_dict.get('disease_name')} Diagnosis"
        session = await create_session(user_id, session_title)
        session_id = session["id"]
    else:
        # Verify ownership
        if db is not None:
            session = await db.chat_sessions.find_one({"_id": session_id, "user_id": user_id})
            if not session:
                session = await db.chat_sessions.find_one({"id": session_id, "user_id": user_id})
                if not session:
                    from ..services.chat_service import create_session
                    session_title = f"{translated_dict.get('disease_name')} Diagnosis"
                    session = await create_session(user_id, session_title)
                    session_id = session["id"]

    # Save user query (upload action) to message history
    from ..services.chat_service import add_message
    user_msg_text = f"Uploaded image for {animal_type} diagnosis"
    image_path = f"/uploads/{filename}"
    await add_message(
        session_id=session_id,
        user_id=user_id,
        role="user",
        text=user_msg_text,
        language=lang,
        text_en=user_msg_text,
        image_url=image_path
    )

    # Build English response representation for context/history tracking
    if disease['name'] == "Healthy":
        english_res_str = f"No disease detected. {disease['animal']} appears healthy."
    else:
        english_res_str = (
            f"I have analyzed your image. It looks like your {disease['animal']} has **{disease['name']}** (Confidence level: {disease['confidence']}%).\n\n"
            f"**Severity:** {disease['severity']}\n\n"
            f"**Symptoms:**\n" + "\n".join([f"- {s}" for s in disease.get("symptoms", [])]) + "\n\n"
            f"**First Aid:**\n" + "\n".join([f"- {f}" for f in disease.get("first_aid", [])]) + "\n\n"
            f"**Suggested Medicine:**\n" + "\n".join([f"- {m}" for m in disease.get("medicine", [])])
        )

    # Save assistant response to message history
    await add_message(
        session_id=session_id,
        user_id=user_id,
        role="assistant",
        text=response_text,
        language=lang,
        text_en=english_res_str
    )

    return {
        "response": response_text,
        "image_url": image_path,
        "disease_name": translated_dict.get("disease_name"),
        "confidence": translated_dict.get("confidence"),
        "session_id": session_id
    }
