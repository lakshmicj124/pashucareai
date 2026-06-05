import sys
sys.path.append(r"c:\Users\DELL\Documents\cow disease project\backend")
from app.services.disease_catalogue import DISEASES

goats = [d for d in DISEASES if d.get("animal") == "Goat"]
cows = [d for d in DISEASES if d.get("animal") == "Cow"]

print(f"Total diseases: {len(DISEASES)}")
print(f"Goats count: {len(goats)}")
print(f"Cows count: {len(cows)}")

# Print first 5 goat diseases
print("\nFirst 5 goat diseases:")
for g in goats[:5]:
    print(f"- {g['name']}")
