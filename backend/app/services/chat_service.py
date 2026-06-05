import datetime
from datetime import timezone
from typing import List, Optional
import httpx
from bson import ObjectId
import logging

from ..database import get_db
from ..config import settings
from .language_service import detect_language
from .translation_service import translate_text

logger = logging.getLogger(__name__)

async def create_session(user_id: str, title: str = "New Chat") -> dict:
    """
    Creates a new chat session for a user.
    """
    db = get_db()
    session_doc = {
        "user_id": user_id,
        "title": title,
        "created_at": datetime.datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.datetime.now(timezone.utc).isoformat()
    }
    
    result = await db.chat_sessions.insert_one(session_doc)
    session_doc["id"] = str(result.inserted_id)
    if "_id" in session_doc:
        del session_doc["_id"]
    return session_doc

async def get_user_sessions(user_id: str) -> List[dict]:
    """
    Fetches all chat sessions for a user, sorted by updated_at descending.
    """
    db = get_db()
    cursor = db.chat_sessions.find({"user_id": user_id})
    sessions = []
    async for doc in cursor:
        doc["id"] = str(doc.get("_id") or doc.get("id"))
        if "_id" in doc:
            del doc["_id"]
        sessions.append(doc)
        
    # Sort sessions by updated_at desc in python for consistency across Mongo/MockDB
    sessions.sort(key=lambda x: x.get("updated_at", ""), reverse=True)
    return sessions

async def get_session_messages(session_id: str) -> List[dict]:
    """
    Retrieves all messages for a specific session, sorted chronologically.
    """
    db = get_db()
    cursor = db.chat_messages.find({"session_id": session_id})
    messages = []
    async for doc in cursor:
        doc["id"] = str(doc.get("_id") or doc.get("id"))
        if "_id" in doc:
            del doc["_id"]
        messages.append(doc)
        
    # Sort chronologically
    messages.sort(key=lambda x: x.get("timestamp", ""))
    return messages

async def delete_session(session_id: str, user_id: str) -> bool:
    """
    Deletes a session and all its associated messages.
    """
    db = get_db()
    # Verify ownership
    session = await db.chat_sessions.find_one({"_id": session_id, "user_id": user_id})
    if not session:
        # Check if ID stored as string in mock db
        session = await db.chat_sessions.find_one({"id": session_id, "user_id": user_id})
        if not session:
            return False
            
    # Delete session
    if hasattr(db.chat_sessions, "delete_one"):
        # MockDB / MongoDB delete_one
        await db.chat_sessions.delete_one({"_id": session_id})
        await db.chat_sessions.delete_one({"id": session_id})
        await db.chat_messages.delete_many({"session_id": session_id})
    return True

async def add_message(session_id: str, user_id: str, role: str, text: str, language: str, text_en: Optional[str] = None, image_url: Optional[str] = None) -> dict:
    """
    Saves a message to the database.
    """
    db = get_db()
    msg_doc = {
        "session_id": session_id,
        "user_id": user_id,
        "role": role,
        "text": text,
        "text_en": text_en or text,
        "language": language,
        "imageUrl": image_url,
        "timestamp": datetime.datetime.now(timezone.utc).isoformat()
    }
    result = await db.chat_messages.insert_one(msg_doc)
    msg_doc["id"] = str(result.inserted_id)
    if "_id" in msg_doc:
        del msg_doc["_id"]
    return msg_doc

def get_local_fallback_response(user_text: str, lang: str = "en", history: Optional[List[dict]] = None) -> str:
    """Provide high-quality local rule-based veterinary responses if Gemini fails."""
    import re
    from .disease_catalogue import DISEASES
    from .translation_service import translate_disease_data
    
    user_text_lower = user_text.lower().strip()
    
    # 1. Greetings (ignoring standalone 'help' if history exists, or check other greeting words)
    greeting_words = ["hello", "hi", "hey", "namaste", "नमस्ते", "हलो", "ಹಲೋ", "ನಮಸ್ಕಾರ"]
    # only include 'help' if there is no session history, otherwise 'help' might mean "help with treatment"
    if not history or len(history) < 2:
        greeting_words.extend(["help", "मदद", "ಸಹಾಯ"])
        
    if any(g in user_text_lower for g in greeting_words):
        if lang == "hi":
            return "नमस्ते! मैं आपका पशुकेयर एआई सहायक हूँ। आज मैं पशु स्वास्थ्य, बीमारी के लक्षणों या प्रबंधन में आपकी क्या मदद कर सकता हूँ?"
        elif lang == "kn":
            return "ನಮಸ್ಕಾರ! ನಾನು ನಿಮ್ಮ ಪಶುಕೇರ್ ಎಐ ಸಹಾಯಕ. ಇಂದು ನಾನು ಜಾನುವಾರುಗಳ ಆರೋಗ್ಯ ಅಥವಾ ನಿರ್ವಹಣೆಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು?"
        else:
            return "Hello! I am your PashuCare AI Assistant. How can I help you with livestock health, animal diseases, symptoms, prevention, or farm management today?"

    # 2. Off-Topic
    off_topic_keywords = [
        "code", "programming", "python", "javascript", "movie", "politics", "sports", "cricket", "weather", "hello world",
        "क्रिकेट", "राजनीति", "मौसम", "फिल्म", "कोडिंग", "प्रोग्रामिंग",
        "ಕ್ರಿಕೆಟ್", "ರಾಜಕೀಯ", "ಹವಾಮಾನ", "ಚಲನಚಿತ್ರ", "ಕೋಡಿಂಗ್", "ಪ್ರೋಗ್ರಾಮಿಂಗ್"
    ]
    if any(ot in user_text_lower for ot in off_topic_keywords):
        if lang == "hi":
            return "मैं केवल पशु स्वास्थ्य और पशुपालन से संबंधित प्रश्नों के उत्तर देने में सक्षम हूँ।"
        elif lang == "kn":
            return "ನಾನು ಪ್ರಾಣಿಗಳ ಆರೋಗ್ಯ ಮತ್ತು ಜಾನುವಾರು ಆರೈಕೆಗೆ ಸಂಬಂಧಿಸಿದ ಪ್ರಶ್ನೆಗಳಿಗೆ ಮಾತ್ರ ಉತ್ತರಿಸಬಲ್ಲೆ."
        else:
            return "I am only programmed to assist with animal health, livestock diseases, symptoms, prevention, recommended feed, and farm management."

    # Disease Mapping Dictionary (handles bilingual exact lookup keys)
    disease_map = {
        "lumpy": "Lumpy Skin Disease",
        "लम्पी": "Lumpy Skin Disease",
        "लंपी": "Lumpy Skin Disease",
        "ಲಂಪಿ": "Lumpy Skin Disease",
        "foot and mouth": "Foot and Mouth Disease",
        "fmd": "Foot and Mouth Disease",
        "खुरपका": "Foot and Mouth Disease",
        "मुँहपका": "Foot and Mouth Disease",
        "ಕಾಲು ಬಾಯಿ": "Foot and Mouth Disease",
        "ಕಾಲಬಾಯಿ": "Foot and Mouth Disease",
        "mastitis": "Mastitis",
        "थनैल": "Mastitis",
        "थनैला": "Mastitis",
        "ಕೆಚ್ಚಲು ಬಾತು": "Mastitis",
        "ಕೆಚ್ಚಲುಬಾತು": "Mastitis",
        "ppr": "Peste des Petits Ruminants (PPR)",
        "पीपीआर": "Peste des Petits Ruminants (PPR)",
        "ಪಿಪಿಆರ್": "Peste des Petits Ruminants (PPR)",
        "bloat": "Bloat (Ruminal Tympany)",
        "अफरा": "Bloat (Ruminal Tympany)",
        "ಹೊಟ್ಟೆ उಬ್ಬರ": "Bloat (Ruminal Tympany)",
        "ಹೊಟ್ಟೆಯುಬ್ಬರ": "Bloat (Ruminal Tympany)",
        "foot rot": "Foot Rot",
        "खुर सड़न": "Foot Rot",
        "ಕಾಲು ಕೊಳೆತ": "Foot Rot",
        "ಕಾಲುಕೊಳೆತ": "Foot Rot",
        "pneumonia": "Pneumonia",
        "निमोनिया": "Pneumonia",
        "ನ್ಯುಮೋನಿಯಾ": "Pneumonia"
    }

    # Determine animal type if specified
    target_animal = None
    if any(k in user_text_lower for k in ["cow", "cattle", "bull", "calf", "गाय", "मवेशी", "ಹಸು", "ಜಾನುವಾರು"]):
        target_animal = "Cow"
    elif any(k in user_text_lower for k in ["goat", "kid", "buck", "बकरी", "बकरा", "ಆಡು", "ಮೇಕೆ"]):
        target_animal = "Goat"
    elif any(k in user_text_lower for k in ["sheep", "lamb", "ewe", "भेड़", "ಕುರಿ"]):
        target_animal = "Sheep"

    best_disease = None
    
    # Method A: Disease trigger keywords mapping
    matched_disease_name = None
    for kw, disease_name in disease_map.items():
        if kw in user_text_lower:
            matched_disease_name = disease_name
            break

    if matched_disease_name:
        for d in DISEASES:
            if d['name'] == matched_disease_name:
                if target_animal and d['animal'] != target_animal:
                    continue
                best_disease = d
                break

    # Method B: Stateful Context Scanning
    if not best_disease and history:
        # Scan history backwards for the last mentioned disease name in assistant responses
        for msg in reversed(history):
            if msg.get("role") == "assistant":
                text_en = (msg.get("text_en") or "").lower()
                matched_diseases = []
                for d in DISEASES:
                    if d['name'].lower() in text_en:
                        matched_diseases.append(d)
                
                if matched_diseases:
                    # Try to find one matching the animal name mentioned in text_en
                    for d in matched_diseases:
                        if d['animal'].lower() in text_en:
                            best_disease = d
                            break
                    if not best_disease:
                        best_disease = matched_diseases[0]
                    break

    # Method C: Token-based scoring match (as last resort)
    if not best_disease:
        def get_words(text):
            raw_words = text.split()
            words = []
            for w in raw_words:
                cleaned = re.sub(r'^[^\w\u0900-\u097F\u0C80-\u0CFF]+|[^\w\u0900-\u097F\u0C80-\u0CFF]+$', '', w)
                if cleaned:
                    words.append(cleaned)
            return set(words)

        concept_map = {
            # Symptoms / Clinical Signs
            "बुखार": ["fever", "temperature"],
            "तापमान": ["fever", "temperature"],
            "ಜ್ವರ": ["fever", "temperature"],
            "गांठें": ["nodule", "nodules", "skin"],
            "गाँठ": ["nodule", "nodules", "skin"],
            "त्वचा": ["skin"],
            "चर्म": ["skin"],
            "ಗಂಟು": ["nodule", "nodules", "skin"],
            "ಚರ್ಮ": ["skin"],
            "लक्षण": ["symptom", "symptoms"],
            "ಲಕ್ಷಣ": ["symptom", "symptoms"],
            "थन": ["udder", "teat", "mastitis"],
            "ಕೆಚ್ಚಲು": ["udder", "teat", "mastitis"],
            "सूजन": ["swelling", "swollen", "edema"],
            "ಬಾತು": ["swelling", "swollen", "edema"],
            "लंगड़ा": ["lame", "lameness", "foot", "hoof"],
            "लंगड़ापन": ["lame", "lameness", "foot", "hoof"],
            "ಕುಂಟು": ["lame", "lameness", "foot", "hoof"],
            "ಕುಂಟುವುದು": ["lame", "lameness", "foot", "hoof"],
            "लार": ["saliva", "salivation", "drool", "drooling"],
            "लार बहना": ["saliva", "salivation", "drool", "drooling"],
            "ಲಾಲಾರಸ": ["saliva", "salivation", "drool", "drooling"],
            "झाग": ["foam", "foaming", "froth", "frothing"],
            "ನೊರೆ": ["foam", "foaming", "froth", "frothing"],
            "भूख": ["appetite", "loss of appetite"],
            "हवा": ["bloat", "tympany"],
            "अफरा": ["bloat", "tympany"],
            "ಹೊಟ್ಟೆ ಉಬ್ಬರ": ["bloat", "tympany"],
            "ಹೊಟ್ಟೆಯುಬ್ಬರ": ["bloat", "tympany"],
            "ಹಸಿವು": ["appetite", "loss of appetite"],
            "दस्त": ["diarrhea", "scours"],
            "ಭೇದಿ": ["diarrhea", "scours"],
            "खांसी": ["cough", "coughing"],
            "ಕೆಮ್ಮು": ["cough", "coughing"],
            "सांस": ["breath", "breathing", "respiratory", "pneumonia"],
            "ಉಸಿರಾಟ": ["breath", "breathing", "respiratory", "pneumonia"],
            "घाव": ["lesion", "lesions", "blister", "blisters", "wound", "wounds"],
            "ಗಾಯ": ["lesion", "lesions", "blister", "blisters", "wound", "wounds"],
            "ಕಜ್ಜಿ": ["scab", "scabies", "itch", "mange"],
            "खुजली": ["scab", "scabies", "itch", "mange"],
            "नाक": ["nasal", "discharge"],
            "ಮೂಗು": ["nasal", "discharge"],
            "स್ರಾವ": ["discharge"],
            "बहना": ["discharge"],
            "आँख": ["ocular", "eye"],
            "ಕಣ್ಣು": ["ocular", "eye"],
            "दूध": ["milk", "yield"],
            "ಹಾಲು": ["milk", "yield"],
            "कमी": ["decrease", "decreased", "loss"],
            "ಕಡಿಮೆ": ["decrease", "decreased", "loss"],
            "कम": ["decrease", "decreased", "loss"],
            "दर्द": ["pain"],
            "ನೋವು": ["pain"],
            "कमजोरी": ["weakness"],
            "ದೌರ್ಬಲ್ಯ": ["weakness"],
            "मुंह": ["mouth", "oral"],
            "ಮುಖ": ["mouth", "oral"],
            "ಬಾಯಿ": ["mouth", "oral"],
            "खुर": ["foot", "hoof", "foot rot", "fmd"],
            "ಕಾಲು": ["foot", "hoof", "foot rot", "fmd"],
            "ಗೊರಸು": ["foot", "hoof", "foot rot", "fmd"],

            # Animals
            "गाय": ["cow", "cattle"],
            "मवेशी": ["cow", "cattle"],
            "ಹಸು": ["cow", "cattle"],
            "ಜಾನುವಾರು": ["cow", "cattle"],
            "बकरी": ["goat"],
            "बकरा": ["goat"],
            "ಆಡು": ["goat"],
            "ಮೇಕೆ": ["goat"],
            "भेड़": ["sheep", "lamb"],
            "ಕುರಿ": ["sheep", "lamb"]
        }

        query_tokens = get_words(user_text_lower)
        
        # Enrich query tokens using concept map
        enriched_tokens = set(query_tokens)
        for token in query_tokens:
            for k, v in concept_map.items():
                if k in token:
                    enriched_tokens.update(v)

        best_score = 0
        for d in DISEASES:
            if target_animal and d['animal'] != target_animal:
                continue
                
            # Perform token matching against translated fields for target language
            d_translated = translate_disease_data(d, lang)
            score = 0
            
            # Match disease name
            name_translated_lower = (d_translated.get('name') or d_translated.get('disease_name') or d['name']).lower()
            name_english_lower = d['name'].lower()
            if name_translated_lower in user_text_lower or name_english_lower in user_text_lower:
                score += 15
                
            # Name token match against both English and translated name
            name_tokens_translated = get_words(name_translated_lower)
            name_tokens_english = get_words(name_english_lower)
            name_intersect = enriched_tokens.intersection(name_tokens_translated.union(name_tokens_english))
            score += len(name_intersect) * 5
            
            # Match symptoms
            symptoms_translated_words = []
            for s in d_translated.get('symptoms', []):
                symptoms_translated_words.extend(get_words(s.lower()))
            symptoms_english_words = []
            for s in d.get('symptoms', []):
                symptoms_english_words.extend(get_words(s.lower()))
                
            symptoms_tokens = set(symptoms_translated_words + symptoms_english_words)
            sym_intersect = enriched_tokens.intersection(symptoms_tokens)
            score += len(sym_intersect) * 2
            
            if score > best_score:
                best_score = score
                best_disease = d
        # Enforce threshold for Method C to filter out weak matches
        if best_score < 3:
            best_disease = None

    # If we matched a disease, construct a tailored diagnostic response based on query keywords
    if best_disease:
        # Translate disease details locally / offline
        translated = translate_disease_data(best_disease, lang)
        
        name = translated.get('name') or translated.get('disease_name') or best_disease['name']
        animal = translated.get('animal') or translated.get('animal_type') or best_disease['animal']
        severity = translated.get('severity') or best_disease['severity']
        
        # Localize animal name if not translated
        if lang == "hi" and animal.lower() == "cow": animal = "गाय"
        elif lang == "hi" and animal.lower() == "goat": animal = "बकरी"
        elif lang == "hi" and animal.lower() == "sheep": animal = "भेड़"
        elif lang == "kn" and animal.lower() == "cow": animal = "ಹಸು"
        elif lang == "kn" and animal.lower() == "goat": animal = "ಆಡು"
        elif lang == "kn" and animal.lower() == "sheep": animal = "ಕುರಿ"

        symptoms = "\n".join([f"- {s}" for s in translated.get('symptoms', [])])
        first_aid = "\n".join([f"- {f}" for f in translated.get('first_aid', [])])
        medicine = "\n".join([f"- {m}" for m in translated.get('medicine', [])])
        prevention = "\n".join([f"- {p}" for p in translated.get('prevention', [])])
        
        causes = "\n".join([f"- {c}" for c in translated.get('causes', [])]) if translated.get('causes') else ""
        why_it_happened = translated.get('why_it_happened', '')
        food_recommendations = "\n".join([f"- {fr}" for fr in translated.get('food_recommendations', [])]) if translated.get('food_recommendations') else ""
        hygiene_tips = "\n".join([f"- {ht}" for ht in translated.get('hygiene_tips', [])]) if translated.get('hygiene_tips') else ""
        emergency = translated.get('emergency', '')

        # Define follow-up keyword lists
        med_kws = [
            "medicine", "treatment", "cure", "drug", "remedy", "remedies", "first aid", "help", "care", 
            "tablet", "injection", "ointment", "syrup", "prescription",
            "दवा", "इलाज", "उपचार", "मरहम", "गोली", "सुझाव", "राहत", "प्राथमिक उपचार",
            "ಔಷಧ", "ಚಿಕಿತ್ಸೆ", "ಪ್ರಥಮ ಚಿಕಿತ್ಸೆ", "ಮಾತ್ರೆ", "ಔಷಧಿ", "ಪರಿಹಾರ"
        ]
        sym_kws = [
            "symptom", "sign", "look like", "clinical sign", "detect", "identify",
            "लक्षण", "निशान", "पहचान",
            "ರೋಗಲಕ್ಷಣ", "ಲಕ್ಷಣ", "ರೋಗಲಕ್ಷಣಗಳು", "ಗುರುತಿಸು"
        ]
        cause_kws = [
            "cause", "why", "reason", "happen", "origin", "source", "how did", "occur",
            "कारण", "क्यों", "कैसे हुआ", "वजह",
            "ಕಾರಣ", "ಏಕೆ", "ಹೇಗೆ ಬಂತು", "ಯಾತಕ್ಕಾಗಿ", "ಹೇಗೆ ಹರಡುತ್ತದೆ"
        ]
        prev_kws = [
            "prevent", "avoid", "stop", "protection", "vaccine", "vaccination", "immunization", "protect",
            "बचाव", "रोकथाम", "टीका", "टीकाकरण", "सुरक्षा",
            "ಲಸಿಕೆ", "ತಡೆಗಟ್ಟ", "ಪರಿಹಾರ", "ತಡೆಗಟ್ಟುವಿಕೆ", "ರಕ್ಷಿಸು"
        ]
        food_kws = [
            "food", "feed", "diet", "eat", "nutrition", "fodder", "browse", "grass", "hay",
            "चारा", "आहार", "खुराक", "खाना", "पोषण",
            "ಖುರಾಕ್", "ಮೇವು", "ಆಹಾರ", "ಊಟ", "ಪೋಷಣೆ"
        ]
        hyg_kws = [
            "hygiene", "clean", "shed", "sanitation", "cleanliness", "bedding",
            "सफाई", "स्वच्छता", "गोबर", "शेड",
            "ಕೊಟ್ಟಿಗೆ", "ಸ್ವಚ್ಛತೆ", "ನೈರ್ಮಲ್ಯ", "ಶುಚಿತ್ವ"
        ]
        name_kws = [
            "disease name", "what is the disease", "what disease", "name", "what is it", "identify",
            "बीमारी का नाम", "रोग का नाम", "बीमारी क्या है", "क्या बीमारी है",
            "ರೋಗದ ಹೆಸರು", "ಯಾವ ರೋಗ", "ರೋಗ ಯಾವುದು", "ರೋಗದ ಹೆಸರೇನು"
        ]
        sev_kws = [
            "severe", "danger", "critical", "severity", "level",
            "गंभीरता", "खतरा", "स्तर",
            "ತೀವ್ರತೆ", "ಅಪಾಯ", "ಮಟ್ಟ"
        ]

        # 1. Medicine / Treatment / First Aid / Cure
        if any(kw in user_text_lower for kw in med_kws):
            if lang == "hi":
                return (
                    f"**{name}** (पशु: {animal}) के लिए उपचार और प्राथमिक उपचार जानकारी:\n\n"
                    f"**प्राथमिक उपचार:**\n{first_aid}\n\n"
                    f"**सुझाई गई दवाएं:**\n{medicine}"
                )
            elif lang == "kn":
                return (
                    f"**{name}** (ಪ್ರಾಣಿ: {animal}) ಗಾಗಿ ಚಿಕಿತ್ಸೆ ಮತ್ತು ಪ್ರಥಮ ಚಿಕಿತ್ಸೆ ಮಾಹಿತಿ:\n\n"
                    f"**ಪ್ರಥಮ ಚಿಕಿತ್ಸೆ:**\n{first_aid}\n\n"
                    f"**ಸೂಚಿಸಲಾದ ಔಷಧಗಳು:**\n{medicine}"
                )
            else:
                return (
                    f"Here is the treatment and first aid information for **{name}** (in {animal}):\n\n"
                    f"**First Aid:**\n{first_aid}\n\n"
                    f"**Recommended Medicine:**\n{medicine}"
                )

        # 2. Symptoms
        elif any(kw in user_text_lower for kw in sym_kws):
            if lang == "hi":
                return f"**{name}** (पशु: {animal}) के मुख्य लक्षण निम्नलिखित हैं:\n\n{symptoms}"
            elif lang == "kn":
                return f"**{name}** (ಪ್ರಾಣಿ: {animal}) ನ ಮುಖ್ಯ ರೋಗಲಕ್ಷಣಗಳು ಈ ಕೆಳಗಿನಂತಿವೆ:\n\n{symptoms}"
            else:
                return f"The main symptoms of **{name}** (in {animal}) are:\n\n{symptoms}"

        # 3. Causes / Why
        elif any(kw in user_text_lower for kw in cause_kws):
            res_parts = []
            if causes:
                if lang == "hi":
                    res_parts.append(f"**{name}** (पशु: {animal}) के मुख्य कारण:\n{causes}")
                elif lang == "kn":
                    res_parts.append(f"**{name}** (ಪ್ರಾಣಿ: {animal}) ತಗಲಲು ಮುಖ್ಯ ಕಾರಣಗಳು:\n{causes}")
                else:
                    res_parts.append(f"Main causes of **{name}** (in {animal}):\n{causes}")
            if why_it_happened:
                if lang == "hi":
                    res_parts.append(f"**यह क्यों हुआ:**\n{why_it_happened}")
                elif lang == "kn":
                    res_parts.append(f"**ಇದು ಏಕೆ ಸಂಭವಿಸಿದೆ:**\n{why_it_happened}")
                else:
                    res_parts.append(f"**Why it happened:**\n{why_it_happened}")
            if res_parts:
                return "\n\n".join(res_parts)
            else:
                if lang == "hi":
                    return f"**{name}** के विशिष्ट कारणों की जानकारी उपलब्ध नहीं है।"
                elif lang == "kn":
                    return f"**{name}** ರೋಗದ ನಿರ್ದಿಷ್ಟ ಕಾರಣಗಳ ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ."
                else:
                    return f"Specific causes for **{name}** are not available."

        # 4. Prevention / Vaccine
        elif any(kw in user_text_lower for kw in prev_kws):
            if lang == "hi":
                return f"**{name}** (पशु: {animal}) से बचाव और रोकथाम के उपाय:\n\n{prevention}"
            elif lang == "kn":
                return f"**{name}** (ಪ್ರಾಣಿ: {animal}) ತಡೆಗಟ್ಟುವಿಕೆ ಮತ್ತು ಮುನ್ನೆಚ್ಚರಿಕೆ ಕ್ರಮಗಳು:\n\n{prevention}"
            else:
                return f"Prevention and control measures for **{name}** (in {animal}):\n\n{prevention}"

        # 5. Food / Diet
        elif any(kw in user_text_lower for kw in food_kws):
            if food_recommendations:
                if lang == "hi":
                    return f"**{name}** (पशु: {animal}) के दौरान पशु के लिए अनुशंसित आहार:\n\n{food_recommendations}"
                elif lang == "kn":
                    return f"**{name}** (ಪ್ರಾಣಿ: {animal}) ಸಮಯದಲ್ಲಿ ಪ್ರಾಣಿಗಳಿಗೆ ಸೂಚಿಸಲಾದ ಆಹಾರಕ್ರಮ:\n\n{food_recommendations}"
                else:
                    return f"Recommended feed and nutrition during **{name}** (in {animal}):\n\n{food_recommendations}"
            else:
                if lang == "hi":
                    return f"**{name}** के लिए कोई विशेष आहार अनुशंसा नहीं है। कृपया सामान्य संतुलित चारा और साफ पानी दें।"
                elif lang == "kn":
                    return f"**{name}** ರೋಗಕ್ಕೆ ಯಾವುದೇ ವಿಶೇಷ ಆಹಾರ ಶಿಫಾರಸು ಇಲ್ಲ. ದಯವಿಟ್ಟು ಸಾಮಾನ್ಯ ಸಮತೋಲಿತ ಮೇವು ಮತ್ತು ಶುದ್ಧ ನೀರನ್ನು ನೀಡಿ."
                else:
                    return f"No special feed recommendations for **{name}**. Please provide normal balanced fodder and clean water."

        # 6. Hygiene / Shed
        elif any(kw in user_text_lower for kw in hyg_kws):
            if hygiene_tips:
                if lang == "hi":
                    return f"**{name}** (पशु: {animal}) के दौरान शेड प्रबंधन और स्वच्छता युक्तियाँ:\n\n{hygiene_tips}"
                elif lang == "kn":
                    return f"**{name}** (ಪ್ರಾಣಿ: {animal}) ಸಮಯದಲ್ಲಿ ಕೊಟ್ಟಿಗೆ ನಿರ್ವಹಣೆ ಮತ್ತು ನೈರ್ಮಲ್ಯ ಸಲಹೆಗಳು:\n\n{hygiene_tips}"
                else:
                    return f"Shed management and hygiene tips during **{name}** (in {animal}):\n\n{hygiene_tips}"
            else:
                if lang == "hi":
                    return f"कृपया पशु के रहने वाले शेड में सामान्य स्वच्छता बनाए रखें, बिछौना सूखा रखें और हवादार वेंटिलेशन सुनिश्चित करें।"
                elif lang == "kn":
                    return f"ದಯವಿಟ್ಟು ಕೊಟ್ಟಿಗೆಯಲ್ಲಿ ಸಾಮಾನ್ಯ ಸ್ವಚ್ಛತೆಯನ್ನು ಕಾಪಾಡಿಕೊಳ್ಳಿ, ಹಾಸಿಗೆಯನ್ನು ಒಣದಾಗಿ ಇರಿಸಿ ಮತ್ತು ಸಾಕಷ್ಟು ಗಾಳಿಯಾಡುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ."
                else:
                    return f"Please maintain general cleanliness in the shed, keep the bedding dry, and ensure adequate ventilation."

        # 7. Disease Name
        elif any(kw in user_text_lower for kw in name_kws):
            if lang == "hi":
                return f"पहचाना गया रोग **{name}** (पशु: {animal}) है।"
            elif lang == "kn":
                return f"ಗುರುತಿಸಲಾದ ರೋಗ **{name}** (ಪ್ರಾಣಿ: {animal})."
            else:
                return f"The identified disease is **{name}** (in {animal})."

        # 8. Severity
        elif any(kw in user_text_lower for kw in sev_kws):
            severity_loc = severity
            if lang == "hi":
                if severity.lower() == "critical": severity_loc = "गंभीर (Critical)"
                elif severity.lower() == "high": severity_loc = "उच्च (High)"
                elif severity.lower() == "moderate": severity_loc = "मध्यम (Moderate)"
                elif severity.lower() == "low": severity_loc = "कम (Low)"
                
                res = f"**{name}** की गंभीरता स्तर: **{severity_loc}**\n\n"
                if emergency:
                    res += f"**आपातकालीन निर्देश:** {emergency}"
                return res
            elif lang == "kn":
                if severity.lower() == "critical": severity_loc = "ಅತಿ ತೀವ್ರ (Critical)"
                elif severity.lower() == "high": severity_loc = "ಹೆಚ್ಚು (High)"
                elif severity.lower() == "moderate": severity_loc = "ಮಧ್ಯಮ (Moderate)"
                elif severity.lower() == "low": severity_loc = "ಕಡಿಮೆ (Low)"
                
                res = f"**{name}** ತೀವ್ರತೆ ಮಟ್ಟ: **{severity_loc}**\n\n"
                if emergency:
                    res += f"**ತುರ್ತು ನಿರ್ದೇಶನಗಳು:** {emergency}"
                return res
            else:
                res = f"The severity level of **{name}** is **{severity}**.\n\n"
                if emergency:
                    res += f"**Emergency Instruction:** {emergency}"
                return res

        # 9. Default rich diagnostic card
        else:
            if lang == "hi":
                res = (
                    f"**पहचाना गया रोग:** {name} (पशु: {animal})\n"
                    f"**गंभीरता:** {severity}\n\n"
                    f"**लक्षण:**\n{symptoms}\n\n"
                    f"**प्राथमिक उपचार:**\n{first_aid}\n\n"
                    f"**दवाएं:**\n{medicine}\n\n"
                    f"**रोकथाम:**\n{prevention}"
                )
                return res
            elif lang == "kn":
                res = (
                    f"**ಗುರುತಿಸಲಾದ ರೋಗ:** {name} (ಪ್ರಾಣಿ: {animal})\n"
                    f"**ತೀವ್ರತೆ:** {severity}\n\n"
                    f"**ರೋಗಲಕ್ಷಣಗಳು:**\n{symptoms}\n\n"
                    f"**ಪ್ರಥಮ ಚಿಕಿತ್ಸೆ:**\n{first_aid}\n\n"
                    f"**ಔಷಧಗಳು:**\n{medicine}\n\n"
                    f"**ತಡೆಗಟ್ಟುವಿಕೆ:**\n{prevention}"
                )
                return res
            else:
                res = (
                    f"**Disease Identified:** {name} (in {animal})\n"
                    f"**Severity:** {severity}\n\n"
                    f"**Symptoms:**\n{symptoms}\n\n"
                    f"**First Aid:**\n{first_aid}\n\n"
                    f"**Recommended Medicine:**\n{medicine}\n\n"
                    f"**Prevention:**\n{prevention}"
                )
                return res

    # If no disease matched, return a friendly default localized message
    if lang == "hi":
        return "मैं आपके संदेश से किसी विशिष्ट बीमारी की पहचान नहीं कर सका। कृपया लक्षणों का अधिक विस्तार से वर्णन करें (जैसे, बुखार, खांसी, त्वचा पर गांठें, लंगड़ापन) ताकि मैं आपकी बेहतर सहायता कर सकूं। वैकल्पिक रूप से, आप सीधे विश्लेषण के लिए पशु की एक छवि अपलोड कर सकते हैं।"
    elif lang == "kn":
        return "ನಿಮ್ಮ ಪ್ರಶ್ನೆಯಿಂದ ನಿರ್ದಿಷ್ಟ ರೋಗವನ್ನು ಗುರುತಿಸಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ದಯವಿಟ್ಟು ರೋಗಲಕ್ಷಣಗಳನ್ನು ವಿವರವಾಗಿ ತಿಳಿಸಿ (ಉದಾಹರಣೆಗೆ ಜ್ವರ, ಕೆಮ್ಮು, ಗಂಟು ಚರ್ಮ, ಕುಂಟುವುದು) ಇದರಿಂದ ನಾನು ನಿಮಗೆ ಉತ್ತಮ ಸಹಾಯ ನೀಡಬಲ್ಲೆ. ಪರ್ಯಾಯವಾಗಿ, ನೀವು ಪ್ರಾಣಿಯ ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಬಹುದು."
    else:
        return "I could not identify a specific disease from your query. Please describe the symptoms in more detail (e.g., fever, coughing, skin nodules, lameness) so I can help you better. Alternatively, you can upload an image of the animal for direct visual analysis."

async def generate_response(session_id: str, user_id: str, message_text: str, lang: Optional[str] = "en") -> str:
    """
    Orchestrates translation, language detection, memory retention, and Gemini content generation.
    """
    db = get_db()
    
    # 1. Detect language
    detected_lang = lang if lang and lang != "auto" else detect_language(message_text)
    
    # 2. Check and prevent duplicate user message submissions within 3 seconds
    history = await get_session_messages(session_id)
    if history:
        last_msg = history[-1]
        if last_msg.get("role") == "user" and last_msg.get("text") == message_text:
            try:
                last_time = datetime.datetime.fromisoformat(last_msg["timestamp"].replace("Z", "+00:00"))
                now = datetime.datetime.now(timezone.utc)
                if (now - last_time).total_seconds() < 3.0:
                    logger.info("Duplicate request detected. Fetching cached assistant response.")
                    # Fetch subsequent assistant response
                    cached_cursor = db.chat_messages.find({
                        "session_id": session_id,
                        "role": "assistant",
                        "timestamp": {"$gt": last_msg["timestamp"]}
                    })
                    cached_msgs = []
                    async for doc in cached_cursor:
                        cached_msgs.append(doc)
                    if cached_msgs:
                        cached_msgs.sort(key=lambda x: x.get("timestamp", ""))
                        return cached_msgs[0]["text"]
            except Exception as e:
                logger.error(f"Error checking duplicate message: {e}")

    # 3. Translate user message to English if it is Hindi/Kannada
    user_msg_en = message_text
    if detected_lang in ["hi", "kn"]:
        user_msg_en = await translate_text(message_text, "en")
        
    # 4. Save original user message
    await add_message(
        session_id=session_id,
        user_id=user_id,
        role="user",
        text=message_text,
        text_en=user_msg_en,
        language=detected_lang
    )

    # 5. Format history context window (last 10 messages) in English
    formatted_contents = []
    # Fetch updated history including the message we just saved
    history = await get_session_messages(session_id)
    context_window = history[-11:-1] if len(history) > 1 else [] # Exclude current user message, send previous turns
    
    for msg in context_window:
        role = "model" if msg["role"] == "assistant" else "user"
        text_to_send = msg.get("text_en") or msg.get("text")
        formatted_contents.append({
            "role": role,
            "parts": [{"text": text_to_send}]
        })
        
    # Append current user message in English
    formatted_contents.append({
        "role": "user",
        "parts": [{"text": user_msg_en}]
    })

    # 6. Call Gemini API in requested language
    lang_names = {
        "hi": "Hindi",
        "kn": "Kannada",
        "en": "English"
    }
    target_name = lang_names.get(detected_lang, "English")

    system_instruction = (
        "You are PashuCare AI Assistant, an expert veterinary AI chatbot. "
        "Only answer questions related to animal health, livestock diseases (e.g., Lumpy Skin, Foot and Mouth, Cow/Goat/Sheep health issues), symptoms, prevention, recommended feed, and livestock shed management. "
        "Provide clear, professional, empathetic, and actionable guidance for farmers. "
        "CRITICAL: If the user asks any off-topic, general, coding, or personal questions unrelated to animal care or livestock, "
        "you must politely refuse to answer and remind them that you are only capable of assisting with animal health and veterinary care."
    )

    if detected_lang in ["hi", "kn"]:
        system_instruction += (
            f"\n\nIMPORTANT: The user selected language is {target_name}. You MUST reply entirely in {target_name}. "
            f"Translate the entire response (disease explanation, symptoms, causes, prevention, feed recommendations, and veterinary guidance) to {target_name}. "
            "Do not mix languages. Do not use English words unless medically/veterinarily necessary (keep standard medicine/drug names if any). "
            f"Ensure all text is written in the correct script ({'Devanagari for Hindi' if detected_lang == 'hi' else 'Kannada script for Kannada'})."
        )

    # Initialize variables
    ai_response_raw = None
    ai_response_translated = None
    ai_response_en = None

    if settings.GEMINI_API_KEY:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={settings.GEMINI_API_KEY}"
        payload = {
            "contents": formatted_contents,
            "systemInstruction": {
                "parts": [{"text": system_instruction}]
            },
            "generationConfig": {
                "temperature": 0.2,
                "maxOutputTokens": 1200
            }
        }
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.post(url, json=payload)
                if response.status_code == 200:
                    res_json = response.json()
                    candidates = res_json.get("candidates", [])
                    if candidates:
                        parts = candidates[0].get("content", {}).get("parts", [])
                        if parts:
                            ai_response_raw = parts[0].get("text", "")
                else:
                    logger.error(f"Gemini API Error: {response.status_code} - {response.text}")
        except Exception as e:
            logger.error(f"Failed to generate content with Gemini: {e}")

    # Fallback to local rule-based disease catalogue matching if Gemini failed or wasn't configured
    if not ai_response_raw:
        logger.info("Gemini API unavailable or failed. Using high-quality local veterinary rule-based fallback.")
        ai_response_translated = get_local_fallback_response(message_text, detected_lang, history)
        ai_response_en = get_local_fallback_response(user_msg_en, "en", history)
    else:
        # Since Gemini generated directly in the target language:
        ai_response_translated = ai_response_raw
        if detected_lang in ["hi", "kn"]:
            ai_response_en = await translate_text(ai_response_raw, "en")
        else:
            ai_response_en = ai_response_raw

    # 8. Save assistant message
    await add_message(
        session_id=session_id,
        user_id=user_id,
        role="assistant",
        text=ai_response_translated,
        text_en=ai_response_en,
        language=detected_lang
    )

    # 9. Update chat session metadata (timestamp and title if it was first message)
    session = await db.chat_sessions.find_one({"_id": session_id})
    if not session:
        session = await db.chat_sessions.find_one({"id": session_id})
        
    if session:
        update_data = {
            "updated_at": datetime.datetime.now(timezone.utc).isoformat()
        }
        # If title is default "New Chat" and this is the first message turn, update title to user message snippet
        if session.get("title") == "New Chat":
            title_snippet = message_text[:30] + "..." if len(message_text) > 30 else message_text
            update_data["title"] = title_snippet
            
        if hasattr(db.chat_sessions, "update_one"):
            # MongoDB
            await db.chat_sessions.update_one({"_id": session.get("_id")}, {"$set": update_data})
        else:
            # Mock DB Collection updates documents directly in memory
            for doc in db.chat_sessions.documents:
                if str(doc.get("_id")) == str(session_id) or str(doc.get("id")) == str(session_id):
                    doc.update(update_data)
            db.chat_sessions._save()

    return ai_response_translated
