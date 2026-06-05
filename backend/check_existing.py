import sys
sys.path.append(r"c:\Users\DELL\Documents\cow disease project\backend")
from app.services.disease_catalogue import DISEASES
import pprint

for d in DISEASES:
    if "weak" in d["name"].lower():
        pprint.pprint(d)
        print("-" * 40)
