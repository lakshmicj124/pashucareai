import sys
import re
sys.path.append(r"c:\Users\DELL\Documents\cow disease project\backend")

from app.services.disease_catalogue import DISEASES
from app.services.translation_service import translate_disease_data, TRANSLATIONS

def clean_tokens(text):
    text = text.lower()
    # Remove common punctuation
    text = re.sub(r'[^\w\s]', ' ', text)
    stop_words = {
        "in", "and", "the", "a", "an", "is", "of", "to", "for", "with", "on", "at", "by", 
        "from", "about", "what", "how", "tell", "me", "or", "has", "have", "my", "your",
        "ಕೋ", "ಮತ್ತೆ", "ಮತ್ತು", "ಗೆ", "को", "और", "में", "से", "का", "की", "के"
    }
    return [w for w in text.split() if len(w) > 0 and w not in stop_words]


def search_disease(user_query, lang="en"):
    query_tokens = clean_tokens(user_query)
    user_text = user_query.lower()
    
    # 1. Determine animal preference from query
    animal_keywords = {
        "cow": ["cow", "cattle", "bovine", "calf", "calves", "bull", "heifer", "गाय", "बैल", "बछड़ा", "ಹಸು", "ಎತ್ತು", "ಕರು"],
        "goat": ["goat", "caprine", "kid", "kids", "buck", "doe", "बकरी", "बकरा", "मेमना", "ಆಡು", "ಮೇಕೆ", "ಮರಿ"],
        "sheep": ["sheep", "ovine", "lamb", "lambs", "ewe", "ewes", "ram", "भेड़", "भेड़ का बच्चा", "ಕುರಿ", "ಕುರಿಮರಿ"]
    }
    
    target_animal = None
    for animal, keywords in animal_keywords.items():
        if any(kw in user_text for kw in keywords):
            target_animal = animal.capitalize()
            break

    best_disease = None
    best_score = -9999
    
    for d in DISEASES:
        # Translate first to match in the user's language
        d_trans = translate_disease_data(d, lang)
        
        score = 0
        
        # Animal match penalty/bonus
        d_animal = d.get("animal", "") # "Cow", "Goat", "Sheep"
        if target_animal:
            if d_animal == target_animal:
                score += 20
            else:
                score -= 100 # Heavy penalty for mismatched animal
        
        # Exact Name Match (contains check on translated name)
        name_trans = d_trans.get("name", "").lower()
        # Clean up parentheses from name for better submatch (e.g. "bloat (ruminal tympany)" -> "bloat")
        name_clean = re.sub(r'\(.*?\)', '', name_trans).strip()
        
        if name_clean in user_text or name_trans in user_text:
            score += 150
        
        # Token-based matches on name
        name_tokens = clean_tokens(name_trans)
        for tok in query_tokens:
            if tok in name_tokens:
                score += 25
        
        # Token-based matches on symptoms
        symptoms_text = " ".join(d_trans.get("symptoms", [])).lower()
        symptom_tokens = clean_tokens(symptoms_text)
        for tok in query_tokens:
            if tok in symptom_tokens:
                score += 10
                
        # Token-based matches on other fields
        other_fields = ["causes", "prevention", "medicine", "first_aid", "why_it_happened"]
        other_text_parts = []
        for field in other_fields:
            val = d_trans.get(field, "")
            if isinstance(val, list):
                other_text_parts.extend(val)
            elif isinstance(val, str):
                other_text_parts.append(val)
        
        other_text = " ".join(other_text_parts).lower()
        other_tokens = clean_tokens(other_text)
        for tok in query_tokens:
            if tok in other_tokens:
                score += 3
        
        if score > best_score:
            best_score = score
            best_disease = d_trans
            
    return best_disease, best_score

# Test cases
tests = [
    ("Tell me about lumpy skin in cows", "en"),
    ("what is ppr?", "en"),
    ("coughing and fever in sheep", "en"),
    ("गाय को थनैला रोग है", "hi"),
    ("ಹಸುವಿಗೆ ಜ್ವರ", "kn"),
    ("how to treat bloat", "en")
]

for q, l in tests:
    sys.stdout.reconfigure(encoding='utf-8')
    # Rank all diseases
    results = []
    for d in DISEASES:
        d_trans = translate_disease_data(d, l)
        
        # Calculate score
        query_tokens = clean_tokens(q)
        user_text = q.lower()
        
        animal_keywords = {
            "cow": ["cow", "cattle", "bovine", "calf", "calves", "bull", "heifer", "गाय", "बैल", "बछड़ा", "ಹಸು", "ಎತ್ತು", "ಕರು"],
            "goat": ["goat", "caprine", "kid", "kids", "buck", "doe", "बकरी", "बकरा", "मेमना", "ಆಡು", "ಮೇಕೆ", "ಮರಿ"],
            "sheep": ["sheep", "ovine", "lamb", "lambs", "ewe", "ewes", "ram", "भेड़", "भेड़ का बच्चा", "ಕುರಿ", "ಕುರಿಮರಿ"]
        }
        
        all_animal_kws = []
        for kws in animal_keywords.values():
            all_animal_kws.extend(kws)
            
        target_animal = None
        for animal, keywords in animal_keywords.items():
            if any(kw in user_text for kw in keywords):
                target_animal = animal.capitalize()
                break
                
        # Filter animal keywords from token list for matching to prevent bias
        match_tokens = [tok for tok in query_tokens if tok not in all_animal_kws]
        
        score = 0
        d_animal = d.get("animal", "")
        if target_animal:
            if d_animal == target_animal:
                score += 20
            else:
                score -= 100
                
        name_trans = d_trans.get("name", "").lower()
        name_clean = re.sub(r'\(.*?\)', '', name_trans).strip()
        
        if name_clean in user_text or name_trans in user_text:
            score += 150
            
        name_tokens = clean_tokens(name_trans)
        for tok in match_tokens:
            if tok in name_tokens:
                score += 25
                
        symptoms_text = " ".join(d_trans.get("symptoms", [])).lower()
        symptom_tokens = clean_tokens(symptoms_text)
        for tok in match_tokens:
            if tok in symptom_tokens:
                score += 10
                
        other_fields = ["causes", "prevention", "medicine", "first_aid", "why_it_happened"]
        other_text_parts = []
        for field in other_fields:
            val = d_trans.get(field, "")
            if isinstance(val, list):
                other_text_parts.extend(val)
            elif isinstance(val, str):
                other_text_parts.append(val)
        
        other_text = " ".join(other_text_parts).lower()
        other_tokens = clean_tokens(other_text)
        for tok in match_tokens:
            if tok in other_tokens:
                score += 3
                
        # Exclude "Healthy" if the query has symptoms (like coughing, fever)
        if d["name"] == "Healthy" and len(match_tokens) > 0:
            score -= 50
            
        results.append((d_trans, score))
        
    results.sort(key=lambda x: x[1], reverse=True)
    print(f"\nQuery: {q} ({l})")
    for idx, (res_d, s) in enumerate(results[:3]):
        print(f"  {idx+1}. Match: {res_d['name']} (Animal: {res_d.get('animal')}, Score: {s})")



