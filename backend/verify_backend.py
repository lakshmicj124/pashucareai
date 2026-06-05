import sys
sys.path.append(r"c:\Users\DELL\Documents\cow disease project\backend")

try:
    from app.services.disease_catalogue import DISEASES
    from app.services.translation_service import translate_disease_data
    
    print(f"Total disease count in catalogue: {len(DISEASES)}")
    
    jaw_swelling_entry = None
    for d in DISEASES:
        if d["name"] == "Jaw Swelling" and d["animal"] == "Goat":
            jaw_swelling_entry = d
            break
            
    if jaw_swelling_entry:
        print("Successfully found 'Jaw Swelling' in catalogue!")
        
        # Test translation to Kannada
        kn_trans = translate_disease_data(jaw_swelling_entry, "kn")
        print("\nKannada Translation:")
        print(f"  Name: {ascii(kn_trans['name'])}")
        print(f"  Symptoms: {ascii(kn_trans['symptoms'])}")
        print(f"  First Aid: {ascii(kn_trans['first_aid'])}")
        
        # Test translation to Hindi
        hi_trans = translate_disease_data(jaw_swelling_entry, "hi")
        print("\nHindi Translation:")
        print(f"  Name: {ascii(hi_trans['name'])}")
        print(f"  Symptoms: {ascii(hi_trans['symptoms'])}")
        print(f"  First Aid: {ascii(hi_trans['first_aid'])}")
    else:
        print("ERROR: 'Jaw Swelling' not found in catalogue.")
        
except Exception as e:
    print(f"Import/Execution error: {e}")
