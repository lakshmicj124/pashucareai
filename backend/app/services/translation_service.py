"""
Translation Service for PashuCare AI.
Provides localizations for disease catalog terms in Kannada (kn) and Hindi (hi).
"""

TRANSLATIONS = {
    "validation": {
        'invalid_animal': {
            'en': 'Invalid image. {detected} detected. Please upload a {expected} image.',
            'hi': 'अमान्य छवि। {detected} का पता चला। कृपया {expected} की तस्वीर अपलोड करें।',
            'kn': 'ಅಮಾನ್ಯ ಚಿತ್ರ. {detected} ಪತ್ತೆಯಾಗಿದೆ. ದಯವಿಟ್ಟು {expected} ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಿ.',
        },
        'animal_not_found': {
            'en': 'Animal not found. Please upload a {expected} image.',
            'hi': 'पशु नहीं मिला। कृपया {expected} की तस्वीर अपलोड करें।',
            'kn': 'ಪ್ರಾಣಿ ಕಂಡುಬಂದಿಲ್ಲ. ದಯವಿಟ್ಟು {expected} ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಿ.',
        },
        'empty_file': {
            'en': 'Empty file uploaded.',
            'hi': 'खाली फ़ाइल अपलोड की गई।',
            'kn': 'ಖಾಲಿ ಫೈಲ್ ಅಪ್ಲೋಡ್ ಮಾಡಲಾಗಿದೆ.',
        },
        'file_too_large': {
            'en': 'File size exceeds 10MB limit.',
            'hi': 'फ़ाइल आकार 10MB सीमा से अधिक है।',
            'kn': 'ಫೈಲ್ ಗಾತ್ರ 10MB ಮಿತಿಗಿಂತ ಹೆಚ್ಚಿದೆ.',
        },
    },
    "kn": {
        'low': 'ಕಡಿಮೆ',
        'moderate': 'ಮಧ್ಯಮ',
        'high': 'ಹೆಚ್ಚು',
        'critical': 'ತುರ್ತು / ತೀವ್ರ',
        'emergency_alert': 'ತುರ್ತು ಪಶುವೈದ್ಯಕೀಯ ಗಮನ ಅಗತ್ಯವಿದೆ: ಈ ಕಾಯಿಲೆಯು ತುಂಬಾ ತೀವ್ರವಾಗಿದೆ. ತಕ್ಷಣ ಪ್ರಾಣಿಯನ್ನು ಪ್ರತ್ಯೇಕಿಸಿ ಮತ್ತು ಪಶುವೈದ್ಯಾಧಿಕಾರಿಗಳನ್ನು ಸಂಪರ್ಕಿಸಿ.',
        'Healthy': 'ಆರೋಗ್ಯಕರ',
        'Foot and Mouth Disease': 'ಕಾಲು ಮತ್ತು ಬಾಯಿ ರೋಗ (ಕಾವಿಕೊರಕ)',
        'Lumpy Skin Disease': 'ಗಂಟು ಚರ್ಮ ರೋಗ',
        'Mastitis': 'ಕೆಚ್ಚಲು ಬಾವು',
        'Bloat (Ruminal Tympany)': 'ಹೊಟ್ಟೆ ಉಬ್ಬರ',
        'Black Quarter (Black Leg)': 'ಚಪ್ಪೆ ರೋಗ',
        'Peste des Petits Ruminants (PPR)': 'ಕುರಿ ಮತ್ತು ಆಡುಗಳ ಪಿಪಿಆರ್ ರೋಗ',
        'Goat Pox': 'ಆಡು ವಾಸೂರಿ',
        'Contagious Ecthyma (Orf)': 'ಸಾಂಕ್ರಾಮಿಕ ಎಕ್ಥಿಮಾ (ಆರ್ಫ್)',
        'Enterotoxemia': 'ರಕ್ತಸ್ರಾವ ವಿಷಾಹರ ರೋಗ',
        'Foot Rot': 'ಕಾಲು ಕೊಳೆತ',
        'Sheep Scab (Psoroptic Mange)': 'ಕುರಿ ಕಜ್ಜಿ',
        'Blue Tongue': 'ನೀಲಿ ನಾಲಿಗೆ ರೋಗ',
        'Pneumonia': 'ನ್ಯುಮೋನಿಯಾ (ಶ್ವಾಸಕೋಶದ ಸೋಂಕು)',
        'The animal is in excellent health due to proper care, good hygiene, and a well-balanced diet.': 'ಸರಿಯಾದ ಕಾಳಜಿ, ಉತ್ತಮ ನೈರ್ಮಲ್ಯ ಮತ್ತು ಸಮತೋಲಿತ ಆಹಾರದಿಂದ ಪ್ರಾಣಿ ಅತ್ಯುತ್ತಮ ಆರೋಗ್ಯದಲ್ಲಿದೆ.',
        'The goat is healthy because of proper herd management, good pasture access, and adequate parasite control.': 'ಸೂಕ್ತ ಮಂದೆ ನಿರ್ವಹಣೆ, ಉತ್ತಮ ಹುಲ್ಲುಗಾವಲು ಪ್ರವೇಶ ಮತ್ತು ಸೂಕ್ತ ಪರಾವಲಂಬಿ ನಿಯಂತ್ರಣದಿಂದ ಆಡು ಆರೋಗ್ಯವಾಗಿದೆ.',
        'The sheep is in optimal health due to good grazing management, effective parasite control, and proper flock care.': 'ಉತ್ತม ಮೇಯಿಸುವಿಕೆ ನಿರ್ವಹಣೆ, ಪರಿಣಾಮಕಾರಿ ಪರಾವಲಂಬಿ ನಿಯಂತ್ರಣ ಮತ್ತು ಸೂಕ್ತ ಹಿಂಡಿನ ಕಾಳಜಿಯಿಂದ ಕುರಿ ಸೂಕ್ತ ಆರೋಗ್ಯದಲ್ಲಿದೆ.',
        'Clear eyes and alert posture': 'ಸ್ಪಷ್ಟ ಕಣ್ಣುಗಳು ಮತ್ತು ಎಚ್ಚರಿಕೆಯ ಭಂಗಿ',
        'Smooth and shiny coat': 'ಮೃದು ಮತ್ತು ಹೊಳೆಯುವ ಚರ್ಮ',
        'Normal breathing and appetite': 'ಸಾಮಾನ್ಯ ಉಸಿರಾಟ ಮತ್ತು ಹಸಿವು',
        'Normal chewing of cud': 'ಸಾಮಾನ್ಯ ಮೆಲಕು ಹಾಕುವುದು',
        'No visible lesions or swelling': 'ಯಾವುದೇ ಗೋಚರ ಗಾಯಗಳು ಅಥವಾ ಊತವಿಲ್ಲ',
        'Active and alert behavior': 'ಸಕ್ರಿಯ ಮತ್ತು ಎಚ್ಚರಿಕೆಯ ನಡವಳಿಕೆ',
        'Normal body temperature (39°C)': 'ಸಾಮಾನ್ಯ ದೇಹದ ಉಷ್ಣತೆ (39°C)',
        'Firm, pelleted feces': 'ಗಟ್ಟಿಯಾದ ಮಲ',
        'Normal appetite and rumination': 'ಸಾಮಾನ್ಯ ಹಸಿವು ಮತ್ತು ಮೆಲಕು',
        'Shiny, smooth coat': 'ಹೊಳೆಯುವ, ಮೃದುವಾದ ಚರ್ಮ',
        'Staying with the flock (not isolated)': 'ಹಿಂಡಿನೊಂದಿಗೆ ಉಳಿಯುವುದು (ಪ್ರತ್ಯೇಕವಾಗಿಲ್ಲ)',
        'Alert and responsive': 'ಎಚ್ಚರಿಕೆ ಮತ್ತು ಸ್ಪಂದಿಸುವಿಕೆ',
        'Normal breathing rate': 'ಸಾಮಾನ್ಯ ಉಸಿರಾಟದ ದರ',
        'Good wool condition without patches': 'ಪ್ಯಾಚ್\u200cಗಳಿಲ್ಲದ ಉತ್ತಮ ಉಣ್ಣೆಯ ಸ್ಥಿತಿ',
        'Even gait without limping': 'ಕುಂಟದೆ ಸಮವಾಗಿ ನಡೆಯುವುದು',
        'Good nutrition and balanced diet': 'ಉತ್ತಮ ಪೋಷಣೆ ಮತ್ತು ಸಮತೋಲಿತ ಆಹಾರ',
        'Proper vaccination schedule': 'ಸರಿಯಾದ ಲಸಿಕೆ ವೇಳಾಪಟ್ಟಿ',
        'Clean and hygienic environment': 'ಸ್ವಚ್ಛ ಮತ್ತು ನೈರ್ಮಲ್ಯದ ವಾತಾವರಣ',
        'Low stress levels': 'ಕಡಿಮೆ ಒತ್ತಡದ ಮಟ್ಟಗಳು',
        'Excellent farm management': 'ಅತ್ಯುತ್ತಮ ಫಾರ್ಮ್ ನಿರ್ವಹಣೆ',
        'Timely vaccination and deworming': 'ಸಕಾಲಿಕ ಲಸಿಕೆ ಮತ್ತು ಜಂತುನಾಶಕ',
        'Nutritious browse and pasture': 'ಪೌಷ್ಟಿಕ ಆಹಾರ ಮತ್ತು ಹುಲ್ಲುಗಾವಲು',
        'Clean and dry housing': 'ಸ್ವಚ್ಛ ಮತ್ತು ಒಣ ವಸತಿ',
        'Optimal flock management': 'ಸೂಕ್ತ ಕುರಿಹಿಂಡು ನಿರ್ವಹಣೆ',
        'Good nutrition and pasture quality': 'ಉತ್ತಮ ಪೋಷಣೆ ಮತ್ತು ಹುಲ್ಲುಗಾವಲು ಗುಣಮಟ್ಟ',
        'Effective parasite control program': 'ಪರಿಣಾಮಕಾರಿ ಪರಾವಲಂಬಿ ನಿಯಂತ್ರಣ ಕಾರ್ಯಕ್ರಮ',
        'Low stress environment': 'ಕಡಿಮೆ ಒತ್ತಡದ ವಾತಾವರಣ',
        'Continue regular health checkups': 'ನಿಯಮಿತ ಆರೋಗ್ಯ ತಪಾಸಣೆ ಮುಂದುವರಿಸಿ',
        'Maintain current feeding schedule': 'ಪ್ರಸ್ತುತ ಆಹಾರ ವೇಳಾಪಟ್ಟಿಯನ್ನು ನಿರ್ವಹಿಸಿ',
        'Keep up with seasonal vaccinations': 'ಕಾಲೋಚಿತ ಲಸಿಕೆಗಳನ್ನು ಹಾಕಿ',
        'Ensure access to clean water': 'ಸ್ವಚ್ಛ ನೀರಿನ ಪ್ರವೇಶವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ',
        'Maintain regular deworming schedule': 'ನಿಯಮಿತ ಜಂತುನಾಶಕ ವೇಳಾಪಟ್ಟಿ ನಿರ್ವಹಿಸಿ',
        'Continue annual vaccinations': 'ವಾರ್ಷಿಕ ಲಸಿಕೆಗಳನ್ನು ಮುಂದುವರಿಸಿ',
        'Provide adequate shelter from extreme weather': 'ವಿಪರೀತ ಹವಾಮಾನದಿಂದ ಸೂಕ್ತ ಆಶ್ರಯ ನೀಡಿ',
        'Trim hooves regularly': 'ನಿಯಮಿತವಾಗಿ ಗೊರಸುಗಳನ್ನು ಕತ್ತರಿಸಿ',
        'Continue routine hoof trimming': 'ನಿಯಮಿತ ಗೊರಸು ಕತ್ತರಿಸುವುದನ್ನು ಮುಂದುವರಿಸಿ',
        'Maintain regular shearing schedule': 'ನಿಯಮಿತ ಉಣ್ಣೆ ಕತ್ತರಿಸುವ ವೇಳಾಪಟ್ಟಿ ನಿರ್ವಹಿಸಿ',
        'Follow flock vaccination protocols': 'ಹಿಂಡಿನ ಲಸಿಕೆ ಪ್ರೋಟೋಕಾಲ್ಗಳನ್ನು ಅನುಸರಿಸಿ',
        'Monitor pasture quality': 'ಹುಲ್ಲುಗಾವಲು ಗುಣಮಟ್ಟವನ್ನು ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ',
        'No medicine required': 'ಯಾವುದೇ ಔಷಧಿ ಅಗತ್ಯವಿಲ್ಲ',
        'Routine deworming (every 3-6 months)': 'ನಿಯಮಿತ ಜಂತುನಾಶಕ (ಪ್ರತಿ 3-6 ತಿಂಗಳಿಗೊಮ್ಮೆ)',
        'Calcium supplements (if lactating)': 'ಕ್ಯಾಲ್ಸಿಯಂ ಪೂರಕಗಳು (ಹಾಲು ನೀಡುತ್ತಿದ್ದರೆ)',
        'Mineral mixture (50g daily)': 'ಖನಿಜ ಮಿಶ್ರಣ (ದಿನಕ್ಕೆ 50 ಗ್ರಾಂ)',
        'No medicine needed': 'ಯಾವುದೇ ಔಷಧಿ ಅಗತ್ಯವಿಲ್ಲ',
        'Routine anthelmintics (deworming)': 'ನಿಯಮಿತ ಜಂತುನಾಶಕ ಔಷಧಗಳು',
        'Vitamin supplements during stress/pregnancy': 'ಒತ್ತಡ/ಗರ್ಭಾವಸ್ಥೆಯಲ್ಲಿ ವಿಟಮಿನ್ ಪೂರಕಗಳು',
        'Copper and zinc supplements if deficient': 'ಕೊರತೆಯಿದ್ದರೆ ತಾಮ್ರ ಮತ್ತು ಸತು ಪೂರಕಗಳು',
        'No medicine necessary': 'ಯಾವುದೇ ಔಷಧಿ ಅಗತ್ಯವಿಲ್ಲ',
        'Routine deworming based on fecal egg counts': 'ಮಲದ ಮೊಟ್ಟೆ ಎಣಿಕೆಗಳ ಆಧಾರದ ಮೇಲೆ ನಿಯಮಿತ ಜಂತುನಾಶಕ',
        'Trace mineral supplements (ensure low copper)': 'ಖನಿಜ ಪೂರಕಗಳು (ಕಡಿಮೆ ತಾಮ್ರವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ)',
        'Vitamin E / Selenium if in deficient area': 'ಕೊರತೆಯಿರುವ ಪ್ರದೇಶದಲ್ಲಿ ವಿಟಮಿನ್ ಇ / ಸೆಲೆನಿಯಮ್',
        'Not applicable': 'ಅನ್ವಯಿಸುವುದಿಲ್ಲ',
        'Monitor daily for any changes': 'ಯಾವುದೇ ಬದಲಾವಣೆಗಳಿಗಾಗಿ ಪ್ರತಿದಿನ ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ',
        'Maintain herd records': 'ಮಂದೆಯ ದಾಖಲೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ',
        'Keep emergency vet contact handy': 'ತುರ್ತು ಪಶುವೈದ್ಯರ ಸಂಪರ್ಕವನ್ನು ಹತ್ತಿರ ಇಟ್ಟುಕೊಳ್ಳಿ',
        'Regularly check for ticks or lice': 'ಉಣ್ಣಿ ಅಥವಾ ಪರೋಪಜೀವಿಗಳಿಗಾಗಿ ನಿಯಮಿತವಾಗಿ ಪರಿಶೀಲಿಸಿ',
        'Monitor body condition score': 'ದೇಹದ ಸ್ಥಿತಿಯ ಸ್ಕೋರ್ ಅನ್ನು ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ',
        'Check hooves for overgrowth': 'ಗೊರಸುಗಳ ಅತಿಯಾದ ಬೆಳவಣಿಗೆಯನ್ನು ಪರಿಶೀಲಿಸಿ',
        'Perform regular body condition scoring': 'ನಿಯಮಿತ ದೇಹದ ಸ್ಥಿತಿ ಸ್ಕೋರಿಂಗ್ ಮಾಡಿ',
        'Check for flystrike during warm months': 'ಬೆಚ್ಚಗಿನ ತಿಂಗಳುಗಳಲ್ಲಿ ಫ್ಲೈಸ್ಟ್ರೈಕ್ಗಾಗಿ ಪರಿಶೀಲಿಸಿ',
        'Monitor lambing ewes closely': 'ಮರಿ ಹಾಕುವ ಕುರಿಗಳನ್ನು ನಿಕಟವಾಗಿ ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಿ',
        'Balanced ratio of green and dry fodder': 'ಹಸಿರು ಮತ್ತು ಒಣ ಮೇವಿನ ಸಮತೋಲಿತ ಅನುಪಾತ',
        'Concentrate feed based on milk yield': 'ಹಾಲಿನ ಇಳುವರಿ ಆಧಾರಿತ ಸಾಂದ್ರೀಕೃತ ಆಹಾರ',
        'Access to fresh, clean drinking water': 'ತಾಜಾ, ಸ್ವಚ್ಛ ಕುಡಿಯುವ ನೀರಿನ ಪ್ರವೇಶ',
        'Provide salt licks': 'ಉಪ್ಪಿನ ನೆಕ್ಕಲುಗಳನ್ನು ಒದಗಿಸಿ',
        'Access to varied browse (shrubs/leaves)': 'ವಿವಿಧ ಪೊದೆಗಳು/ಎಲೆಗಳ ಮೇವು',
        'High-quality grass hay': 'ಉತ್ತಮ ಗುಣಮಟ್ಟದ ಒಣ ಹುಲ್ಲು',
        'Loose goat-specific minerals': 'ಆಡು-ನಿರ್ದಿಷ್ಟ ಸಡಿಲ ಖನಿಜಗಳು',
        'Clean, fresh water always': 'ಯಾವಾಗಲೂ ಸ್ವಚ್ಛ, ತಾಜಾ ನೀರು',
        'High quality pasture grazing': 'ಉತ್ತಮ ಗುಣಮಟ್ಟದ ಹುಲ್ಲುಗಾವಲು ಮೇಯಿಸುವಿಕೆ',
        'Supplemental hay during winter/drought': 'ಚಳಿಗಾಲ/ಬರಗಾಲದಲ್ಲಿ ಪೂರಕ ಒಣ ಹುಲ್ಲು',
        'Sheep-specific mineral mix (no added copper)': 'ಕುರಿ-ನಿರ್ದಿಷ್ಟ ಖನಿಜ ಮಿಶ್ರಣ (ಹೆಚ್ಚುವರಿ ತಾಮ್ರವಿಲ್ಲದೆ)',
        'Fresh, unfrozen water access': 'ತಾಜಾ ನೀರಿನ ಪ್ರವೇಶ',
        'Daily cleaning of the shed': 'ಕೊಟ್ಟಿಗೆಯ ದಿನನಿತ್ಯದ ಸ್ವಚ್ಛತೆ',
        'Proper disposal of dung': 'ಗೊಬ್ಬರದ ಸರಿಯಾದ ವಿಲೇವಾರಿ',
        'Regular grooming/brushing of the cow': 'ಹಸುವನ್ನು ನಿಯಮಿತವಾಗಿ ತೊಳೆಯುವುದು/ಸ್ವಚ್ಛಗೊಳಿಸುವುದು',
        'Maintain dry and comfortable bedding': 'ಒಣ ಮತ್ತು ಆರಾಮದಾಯಕ ಹಾಸಿಗೆಯನ್ನು ನಿರ್ವಹಿಸಿ',
        'Keep pens dry and well-ventilated': 'ಪೆನ್ನುಗಳನ್ನು ಒಣದಾಗಿ ಮತ್ತು ಉತ್ತಮ ಗಾಳಿ ಬೀಸುವಂತೆ ಇಡಿ',
        'Clean water troughs daily': 'ನೀರಿನ ತೊಟ್ಟಿಗಳನ್ನು ಪ್ರತಿದิน ಸ್ವಚ್ಛಗೊಳಿಸಿ',
        'Disinfect kidding pens before use': 'ಬಳಕೆಗೆ ಮೊದಲು ಮರಿ ಹಾಕುವ ಪೆನ್ನುಗಳನ್ನು ಸೋಂಕುರಹಿತಗೊಳಿಸಿ',
        'Manage pasture rotation to reduce parasites': 'پರಾವಲಂಬಿಗಳನ್ನು ಕಡಿಮೆ ಮಾಡಲು ಹುಲ್ಲುಗಾವಲು ಸರದಿಯನ್ನು ನಿರ್ವಹಿಸಿ',
        'Keep housing well-ventilated and dry': 'ವಸತಿಯನ್ನು ಉತ್ತಮ ಗಾಳಿ ಬೀಸುವಂತೆ ಮತ್ತು ಒಣದಾಗಿ ಇಡಿ',
        'Provide clean, dry bedding': 'ಸ್ವಚ್ಛವಾದ, ಒಣ ಹಾಸಿಗೆಯನ್ನು ಒದಗಿಸಿ',
        'Use footbaths routinely to prevent hoof issues': 'ಗೊರಸು ಸಮಸ್ಯೆಗಳನ್ನು ತಡೆಗಟ್ಟಲು ನಿಯಮಿತವಾಗಿ ಕಾಲು ಸ್ನಾನ ಬಳಸಿ',
        'Shear before hot weather to prevent heat stress': 'ಶಾಖದ ಒತ್ತಡವನ್ನು ತಡೆಗಟ್ಟಲು ಬಿಸಿ ವಾತಾವರಣಕ್ಕೂ ಮುನ್ನ ಉಣ್ಣೆ ಕತ್ತರಿಸಿ',
        'Jaw Swelling': 'ದವಡೆ ಬಾವು',
        'Kicking at Abdomen': 'ಹೊಟ್ಟೆಗೆ ಒದೆಯುವುದು',
        'Lethargy Syndrome': 'ಆಲಸ್ಯ ಸಿಂಡ್ರೋಮ್',
        'Limb Weakness': 'ಕಾಲುಗಳ ದೌರ್ಬಲ್ಯ',
        'Loss of Appetite': 'ಹಸಿವು ಇಲ್ಲದಿರುವುದು',
        'Mouth Foaming': 'ಬಾಯಲ್ಲಿ ನೊರೆ ಬರುವುದು',
        'Muscle Atrophy': 'ಸ್ನಾಯು ಕ್ಷೀಣತೆ',
        'Muscle Rigidity': 'ಸ್ನಾಯು ಬಿಗಿತ',
        'Nasal Discharge': 'ಮೂಗಿನಿಂದ ದ್ರವ ಸೋರುವುದು',
        'Neck Rigidity': 'ಕುತ್ತಿಗೆ ಬಿಗಿತ',
        'Nervous Tremors': 'ನರಗಳ ನಡುಕ',
        'Night Blindness': 'ಇರುಳು ಕುರುಡುತನ',
        'Enlargement of jaw region': 'ದವಡೆಯ ಭಾಗ ದೊಡ್ಡದಾಗುವುದು',
        'Pain while chewing': 'ಮೆಲಕು ಹಾಕುವಾಗ ನೋವು',
        'Signs of abdominal pain and discomfort': 'ಹೊಟ್ಟೆ ನೋವು ಮತ್ತು ಅಸ್ವಸ್ಥತೆಯ ಲಕ್ಷಣಗಳು',
        'Restlessness': 'ಬೇಚೆನಿತನ (ಅಶಾಂತಿ)',
        'Lying down and getting up frequently': 'ಪದೇ ಪದೇ ಮಲಗುವುದು ಮತ್ತು ಏಳುವುದು',
        'Extreme tiredness': 'ವಿಪರೀತ ಆಯಾಸ',
        'Reduced activity': 'ಕಡಿಮೆ ಚಟುವಟಿಕೆ',
        'Reluctance to move or stand': 'ಚಲಿಸಲು ಅಥವಾ ನಿಲ್ಲಲು ಹಿಂಜರಿಕೆ',
        'Difficulty standing or walking': 'ನಿಲ್ಲಲು ಅಥವಾ ನಡೆಯಲು ತೊಂದರೆ',
        'Incoordination': 'ಅಸಮನ್ವಯತೆ',
        'Stumbling or weakness in legs': 'ಕಾಲುಗಳಲ್ಲಿ ಮುಗ್ಗರಿಸುವುದು ಅಥವಾ ದೌರ್ಬಲ್ಯ',
        'Reduced or no feed intake': 'ಆಹಾರ ಸೇವನೆ ಕಡಿಮೆಯಾಗುವುದು ಅಥವಾ ನಿಲ್ಲುವುದು',
        'Dullness': 'ಆಲಸ್ಯ',
        'Reduced rumination': 'ಮೆಲಕು ಹಾಕುವುದು ಕಡಿಮೆಯಾಗುವುದು',
        'Frothy saliva around mouth': 'ಬಾಯಿಯ ಸುತ್ತ ನೊರೆ ಲಾಲಾರಸ',
        'Excessive salivation': 'ಅತಿಯಾದ ಲಾಲಾರಸ ಸ್ರವಿಸುವಿಕೆ',
        'Choking signs': 'ಉಸಿರುಗಟ್ಟುವಿಕೆಯ ಲಕ್ಷಣಗಳು',
        'Loss of muscle mass over time': 'ಕಾಲಾನಂತರದಲ್ಲಿ ಸ್ನಾಯುವಿನ ದ್ರವ್ಯರಾಶಿ ನಷ್ಟ',
        'Weight loss': 'ತೂಕ ನಷ್ಟ',
        'Visible bony prominences': 'ಮೂಳೆಗಳು ಎದ್ದು ಕಾಣುವುದು',
        'Stiff and tight muscles': 'ಬಿಗಿಯಾದ ಮತ್ತು ಬಿಗಿಯಾದ ಸ್ನಾಯುಗಳು',
        'Sawhorse stance': 'ಸಾವ್\u200cಹಾರ್ಸ್ ಭಂಗಿ',
        'Difficulty bending limbs or neck': 'ಅಂಗಗಳನ್ನು ಅಥವಾ ಕುತ್ತಿಗೆಯನ್ನು ಬಗ್ಗಿಸಲು ತೊಂದರೆ',
        'Mucus or pus coming from nostrils': 'ಮೂಗಿನ ಹೊಳ್ಳೆಗಳಿಂದ ಲೋಳೆ ಅಥವಾ ಕೀವು ಬರುವುದು',
        'Sneezing': 'ಸೀನುವುದು',
        'Coughing': 'ಕೆಮ್ಮುವುದು',
        'Difficulty moving neck freely': 'ಕುತ್ತಿಗೆಯನ್ನು ಮುಕ್ತವಾಗಿ ಚಲಿಸಲು ತೊಂದರೆ',
        'Stiff neck (torticollis)': 'ಬಿಗಿ ಕುತ್ತಿಗೆ (ಟಾರ್ಟಿಕೊಲಿಸ್)',
        'Star-gazing posture': 'ಸ್ಟಾರ್-ಗೇಜಿಂಗ್ ಭಂಗಿ',
        'Involuntary shaking movements': 'ಅನೈಚ್ಛಿಕ ನಡುಕ ಚಲನೆಗಳು',
        'Muscle twitching': 'ಸ್ನಾಯು ಸೆಳೆತ',
        'Shivering-like motions': 'ನಡುಕ ತರಹದ ಚಲನೆಗಳು',
        'Poor vision in low light': 'ಕಡಿಮೆ ಬೆಳಕಿನಲ್ಲಿ ಕಳಪೆ ದೃಷ್ಟಿ',
        'Bumping into objects at dusk': 'ಮುಸ್ಸಂಜೆಯಲ್ಲಿ ವಸ್ತುಗಳಿಗೆ ಡಿಕ್ಕಿ ಹೊಡೆಯುವುದು',
        'Dilated pupils that react slowly': 'ನಿಧಾನವಾಗಿ ಪ್ರತಿಕ್ರಿಯಿಸುವ ಹಿಗ್ಗಿದ ಕಣ್ಣಿನ ಪಾಪೆಗಳು',
        'Coarse or abrasive feed injuring oral cavity': 'ಒರಟಾದ ಆಹಾರವು ಬಾಯಿಯ ಕುಹರಕ್ಕೆ ಹಾನಿ ಮಾಡುತ್ತದೆ',
        'Bacterial infection (e.g., Actinomyces/lumpy jaw)': 'ಬ್ಯಾಕ್ಟೀರಿಯಾ ಸೋಂಕು (ಉದಾಹರಣೆಗೆ, ಆಕ್ಟಿನೊಮೈಸೆಸ್/ದವಡೆ ಬಾವು)',
        'Dental issues or tooth root abscess': 'ಹಲ್ಲಿನ ತೊಂದರೆಗಳು ಅಥವಾ ಹಲ್ಲಿನ ಬೇರಿನ ಕೀವು ಕೋಶ',
        'Ruminal impaction or severe bloat': 'ಹೊಟ್ಟೆಯ ಗಟ್ಟಿ ಮುದ್ದೆ ಅಥವಾ ತೀವ್ರ ಉಬ್ಬರ',
        'Gastrointestinal parasites': 'ಜಠರಗರುಳಿನ ಪರಾವಲಂಬಿಗಳು',
        'Ingestion of toxic plants or foreign objects': 'ವಿಷಕಾರಿ ಸಸ್ಯಗಳು ಅಥವಾ ಹೊರಗಿನ ವಸ್ತುಗಳ ಸೇವನೆ',
        'Systemic infection or chronic disease': 'ವ್ಯವಸ್ಥಿತ ಸೋಂಕು ಅಥವಾ ದೀರ್ಘಕಾಲದ ಕಾಯಿಲೆ',
        'Nutritional deficiencies': 'ಪೌಷ್ಟಿಕಾಂಶದ ಕೊರತೆಗಳು',
        'Severe heat stress or dehydration': 'ತೀವ್ರ ತಾಪಮಾನ ಒತ್ತಡ ಅಥವಾ ನಿರ್ಜಲೀಕರಣ',
        'Metabolic imbalances (e.g., calcium/magnesium deficiency)': 'ಚಯಾಪಚಯ ಅಸಮತೋಲನ (ಉದಾಹರಣೆಗೆ, ಕ್ಯಾಲ್ಸಿಯಂ/ಮೆಗ್ನೀಸಿಯಮ್ ಕೊರತೆ)',
        'Neurological disorders or spinal injury': 'ನರರೋಗ ಅಸ್ವಸ್ಥತೆಗಳು ಅಥವಾ ಬೆನ್ನುಹುರಿಯ ಗಾಯ',
        'Infectious arthritis or joint ill': 'ಸಾಂಕ್ರಾಮಿಕ ಸಂಧಿವಾತ ಅಥವಾ ಕೀಲು ನೋವು',
        'Fever or underlying infectious disease': 'ಜ್ವರ ಅಥವಾ ಆಂತರಿಕ ಸಾಂಕ್ರಾಮಿಕ ರೋಗ',
        'Rumen acidosis or digestive upset': 'ರುಮೆನ್ ಆಮ್ಲೀಯತೆ ಅಥವಾ ಜೀರ್ಣಕ್ರಿಯೆ ಅಸ್ವಸ್ಥತೆ',
        'Stress or dental pain': 'ಒತ್ತಡ ಅಥವಾ ಹಲ್ಲಿನ ನೋವು',
        'Ingestion of organophosphate pesticides or toxic plants': 'ಆರ್ಗನೋಫಾಸ್ಫೇಟ್ ಕೀಟನಾಶಕಗಳು ಅಥವಾ ವಿಷಕಾರಿ ಸಸ್ಯಗಳ ಸೇವನೆ',
        'Rabies or other neurological infections': 'ರೇಬೀಸ್ ಅಥವಾ ಇತರ ನರರೋಗ ಸೋಂಕುಗಳು',
        'Esophageal obstruction (choking)': 'ಅನ್ನನಾಳದ ಅಡಚಣೆ (ಉಸಿರುಗಟ್ಟುವಿಕೆ)',
        'Chronic internal parasitism (worms/flukes)': 'ದೀರ್ಘಕಾಲದ ಆಂತರಿಕ ಪರಾವಲಂಬಿ ಸೋಂಕು (ಹುಳುಗಳು)',
        'Malnutrition or protein deficiency': 'ಅಪೌಷ್ಟಿಕತೆ ಅಥವಾ ಪ್ರೋಟೀನ್ ಕೊರತೆ',
        "Chronic debilitating diseases (like Johne's disease)": 'ದೀರ್ಘಕಾಲದ ವೀಕ್ನೆಸ್ ಉಂಟುಮಾಡುವ ಕಾಯಿಲೆಗಳು (ಜೋನ್ಸ್ ಕಾಯಿಲೆಯಂತೆ)',
        'Tetanus (Clostridium tetani infection)': 'ಧನುರ್ವಾಯು (ಕ್ಲೋಸ್ಟ್ರಿಡಿಯಮ್ ಟೆಟಾನಿ ಸೋಂಕು)',
        'Strychnine poisoning or toxic plant ingestion': 'ಸ್ಟ್ರಿಕ್ನಿನ್ ವಿಷ ಅಥವಾ ವಿಷಕಾರಿ ಸಸ್ಯದ ಸೇವನೆ',
        'Severe electrolyte imbalance': 'ತೀವ್ರ ವಿದ್ಯುದ್ವಿಭಜನೆ ಅಸಮತೋಲನ',
        'Respiratory tract infections (pasteurellosis/pneumonia)': 'ಉಸಿರಾಟದ ಸೋಂಕುಗಳು (ನ್ಯುಮೋನಿಯಾ)',
        'Nasal bot infestation (Oestrus ovis)': 'ಮೂಗಿನ ನೊಣ ಸೋಂಕು (ಈಸ್ಟ್ರಸ್ ಓವಿಸ್)',
        'Dusty or poorly ventilated housing': 'ಧೂಳು ತುಂಬಿದ ಅಥವಾ ಕಳಪೆ ಗಾಳಿ ಇರುವ ಕೊಟ್ಟಿಗೆ',
        'Polioencephalomalacia (PEM / Thiamine deficiency)': 'ಪೋಲಿಯೊಎನ್ಸೆಫಲೋಮಾಲಸಿಯಾ (ಥಯಾಮಿನ್ ಕೊರತೆ)',
        'Listeriosis (circling disease)': 'ಲಿಸ್ಟರಿಯೊಸಿಸ್ (ಸುತ್ತುವ ರೋಗ)',
        'Meningitis or spinal trauma': 'ಮೆನಿಂಜೈಟಿಸ್ ಅಥವಾ ಬೆನ್ನುಹುರಿಯ ಆಘಾತ',
        'Neurological toxicities (mycotoxins/poisonous plants)': 'ನರರೋಗ ವಿಷತ್ವಗಳು (ವಿಷಕಾರಿ ಸಸ್ಯಗಳು)',
        'Metabolic disorders (hypomagnesemia/hypocalcemia)': 'ಚಯಾಪಚಯ ಅಸ್ವಸ್ಥತೆಗಳು (ಹೈಪೋಮ್ಯಾಗ್ನೇಸೀಮಿಯಾ)',
        'Infectious encephalitic diseases': 'ಸಾಂಕ್ರಾಮಿಕ ಮಿದುಳು ಜ್ವರ ರೋಗಗಳು',
        'Vitamin A deficiency': 'ವಿಟಮಿನ್ ಎ ಕೊರತೆ',
        'Infectious keratoconjunctivitis (pink eye)': 'ಸಾಂಕ್ರಾಮಿಕ ಕಣ್ಣಿನ ಸೋಂಕು (ಗುಲಾಬಿ ಕಣ್ಣು)',
        'Congenital eye defects': 'ಜನ್ಮಜಾತ ಕಣ್ಣಿನ ದೋಷಗಳು',
        'The goat developed jaw swelling due to a bacterial infection entering through a scratch in the mouth or a dental injury.': 'ಬಾಯಿಯಲ್ಲಿ ಗೀರು ಅಥವಾ ಹಲ್ಲಿನ ಗಾಯದ ಮೂಲಕ ಬ್ಯಾಕ್ಟೀರಿಯಾದ ಸೋಂಕು ಪ್ರವೇಶಿಸಿದ್ದರಿಂದ ಮೇಕೆಗೆ ದವಡೆ ಬಾವು ಕಾಣಿಸಿಕೊಂಡಿದೆ.',
        'The goat is showing signs of severe colic or abdominal distress, which could be due to gas accumulation, impaction, or parasitic infection.': 'ಮೇಕೆ ತೀವ್ರವಾದ ಹೊಟ್ಟೆ ನೋವು ಅಥವಾ ಜಠರಗರುಳಿನ ತೊಂದರೆಯ ಲಕ್ಷಣಗಳನ್ನು ತೋರಿಸುತ್ತಿದೆ, ಇದು ಅನಿಲ ಸಂಗ್ರಹಣೆ ಅಥವಾ ಪರಾವಲಂಬಿ ಸೋಂಕಿನಿಂದ ಇರಬಹುದು.',
        'The goat is experiencing extreme tiredness and reduced activity, indicating an underlying systemic infection, metabolic issue, or high fever.': 'ಮೇಕೆ ತೀವ್ರ ಆಯಾಸ ಮತ್ತು ಕಡಿಮೆ ಚಟುವಟಿಕೆಯನ್ನು ಅನುಭವಿಸುತ್ತಿದೆ, ಇದು ಆಂತರಿಕ ಸೋಂಕು ಅಥವಾ ಹೆಚ್ಚಿನ ಜ್ವರವನ್ನು ಸೂಚಿಸುತ್ತದೆ.',
        'The goat has difficulty standing or walking due to muscle weakness, joint inflammation, or neurological impairment.': 'ಸ್ನಾಯು ದೌರ್ಬಲ್ಯ, ಕೀಲುಗಳ ಉರಿಯೂತ ಅಥವಾ ನರಗಳ ತೊಂದರೆಯಿಂದ ಮೇಕೆಗೆ ನಿಲ್ಲಲು ಅಥವಾ ನಡೆಯಲು ತೊಂದರೆಯಾಗುತ್ತಿದೆ.',
        'The goat has stopped eating, which is a primary indicator of pain, fever, metabolic disturbance, or stress.': 'ಮೇಕೆ ಆಹಾರ ಸೇವನೆಯನ್ನು ನಿಲ್ಲಿಸಿದೆ, ಇದು ನೋವು, ಜ್ವರ ಅಥವಾ ಒತ್ತಡದ ಪ್ರಾಥಮಿಕ ಸೂಚಕವಾಗಿದೆ.',
        'The goat is foaming at the mouth, which suggests acute poisoning, a severe neurological condition, or a physical blockage in the throat.': 'ಮೇಕೆಯ ಬಾಯಲ್ಲಿ ನೊರೆ ಬರುತ್ತಿದೆ, ಇದು ತೀವ್ರ ವಿಷ ಸೇವನೆ ಅಥವಾ ಗಂಟಲಿನಲ್ಲಿನ ಅಡಚಣೆಯನ್ನು ಸೂಚಿಸುತ್ತದೆ.',
        'The goat is losing muscle mass over time due to chronic nutrient malabsorption, poor diet, or a long-term wasting infection.': 'ದೀರ್ಘಕಾಲದ ಪೌಷ್ಟಿಕಾಂಶದ ಹೀರಿಕೊಳ್ಳುವಿಕೆಯ ಕೊರತೆ ಅಥವಾ ಕಳಪೆ ಆಹಾರದಿಂದ ಮೇಕೆ ಕಾಲಾನಂತರದಲ್ಲಿ ಸ್ನಾಯುವಿನ ದ್ರವ್ಯರಾಶಿಯನ್ನು ಕಳೆದುಕೊಳ್ಳುತ್ತಿದೆ.',
        'The goat exhibits stiff and rigid muscles, which is a classic sign of tetanus infection, typically entering through an untreated wound or castration site.': 'ಮೇಕೆ ಬಿಗಿಯಾದ ಸ್ನಾಯುಗಳನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತದೆ, ಇದು ಧನುರ್ವಾಯು ಸೋಂಕಿನ ಶ್ರೇಷ್ಠ ಸಂಕೇತವಾಗಿದೆ, ಸಾಮಾನ್ಯವಾಗಿ ಚಿಕಿತ್ಸೆ ನೀಡದ ಗಾಯದ ಮೂಲಕ ಪ್ರವೇಶಿಸುತ್ತದೆ.',
        'The goat has nasal discharge due to irritation or infection in its upper or lower respiratory tract.': 'ಉಸಿರಾಟದ ಪ್ರದೇಶದಲ್ಲಿ ಉರಿ ಅಥವಾ ಸೋಂಕಿನ ಕಾರಣ ಮೇಕೆಯ ಮೂಗಿನಿಂದ ದ್ರವ ಸೋರುತ್ತಿದೆ.',
        'The goat has neck rigidity or abnormal posture, indicating a neurological disturbance, commonly thiamine deficiency or brain infection.': 'ಮೇಕೆಗೆ ಕುತ್ತಿಗೆ ಬಿಗಿತ ಅಥವಾ ಅಸಹಜ ಭಂಗಿ ಇದೆ, ಇದು ನರರೋಗ ತೊಂದರೆ ಅಥವಾ ಮೆದುಳಿನ ಸೋಂಕನ್ನು ಸೂಚಿಸುತ್ತದೆ.',
        'The goat exhibits shaking and twitching due to nervous system overstimulation, which can be caused by toxins, mineral lack, or brain inflammation.': 'ವಿಷಗಳು ಅಥವಾ ಮೆದುಳಿನ ಉರಿಯೂತದಿಂದಾಗಿ ನರಮಂಡಲದ ಅತಿಯಾದ ಪ್ರಚೋದನೆಯಿಂದ ಮೇಕೆ ನಡುಕ ಮತ್ತು ಸೆಳೆತವನ್ನು ಪ್ರದರ್ಶಿಸುತ್ತಿದೆ.',
        'The goat has poor vision in dim light, which is a classic symptom of vitamin A deficiency due to lack of green fodder.': 'ಹಸಿರು ಮೇವಿನ ಕೊರತೆಯಿಂದಾಗಿ ವಿಟಮಿನ್ ಎ ಕೊರತೆಯ ಕ್ಲಾಸಿಕ್ ಲಕ್ಷಣವಾದ ಕಡಿಮೆ ಬೆಳಕಿನಲ್ಲಿ ಮೇಕೆಗೆ ಕಳಪೆ ದೃಷ್ಟಿ ಇದೆ.',
        'Avoid feeding extremely coarse or thorny forage': 'ಅತಿಯಾದ ಒರಟಾದ ಅಥವಾ ಮುಳ್ಳಿನ ಮೇವನ್ನು ನೀಡುವುದನ್ನು ತಪ್ಪಿಸಿ',
        'Regularly inspect teeth and mouth for injuries': 'ಚರ್ಮ ಅಥವಾ ಬಾಯಿಯ ಗಾಯಗಳಿಗಾಗಿ ನಿಯಮಿತವಾಗಿ ಹಲ್ಲುಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ',
        'Maintain clean feeding troughs': 'ಮೇವು ತಿನ್ನುವ ತೊಟ್ಟಿಗಳನ್ನು ಸ್ವಚ್ಛವಾಗಿಡಿ',
        'Provide a balanced diet and avoid sudden feed changes': 'ಸಮತೋಲಿತ ಆಹಾರವನ್ನು ಒದಗಿಸಿ ಮತ್ತು ಹಠಾತ್ ಆಹಾರ ಬದಲಾವಣೆಗಳನ್ನು ತಪ್ಪಿಸಿ',
        'Implement a regular deworming schedule': 'ನಿಯಮಿತ ಜಂತುನಾಶಕ ವೇಳಾಪಟ್ಟಿಯನ್ನು ಜಾರಿಗೆ ತರಲು',
        'Ensure constant access to clean water': 'ಯಾವಾಗಲೂ ಸ್ವಚ್ಛ ನೀರಿನ ಲಭ್ಯತೆಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ',
        'Provide a clean, well-ventilated housing': 'ಸ್ವಚ್ಛವಾದ, ಉತ್ತಮ ಗಾಳಿ ಇರುವ ವಸತಿಯನ್ನು ಒದಗಿಸಿ',
        'Ensure adequate nutrition and mineral supplements': 'ಸಾಕಷ್ಟು ಪೋಷಣೆ ಮತ್ತು ಖನಿಜ ಪೂರಕಗಳನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ',
        'Keep water clean and accessible': 'ನೀರನ್ನು ಸ್ವಚ್ಛವಾಗಿ ಮತ್ತು ಲಭ್ಯವಿರುವಂತೆ ಇಡಿ',
        'Ensure balanced mineral intake, especially for pregnant/lactating goats': 'ಗರ್ಭಿಣಿ/ಹಾಲುಣಿಸುವ ಮೇಕೆಗಳಿಗೆ ಸಮತೋಲಿತ ಖನಿಜ ಸೇವನೆಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ',
        'Maintain dry and clean bedding to prevent joint infections': 'ಕೀಲು ಸೋಂಕುಗಳನ್ನು ತಡೆಗಟ್ಟಲು ಒಣ ಮತ್ತು ಸ್ವಚ್ಛವಾದ ಹಾಸಿಗೆಯನ್ನು ನಿರ್ವಹಿಸಿ',
        'Keep paths clear of hazards': 'ಮಾರ್ಗಗಳನ್ನು ಅಪಾಯಗಳಿಂದ ಮುಕ್ತವಾಗಿಡಿ',
        'Introduce new feed gradually': 'ಹೊಸ ಮೇವನ್ನು ಕ್ರಮೇಣ ಪರಿಚಯಿಸಿ',
        'Avoid moldy or spoiled feed': 'ಬೂಷ್ಟು ಹಿಡಿದ ಅಥವಾ ಹಾಳಾದ ಆಹಾರವನ್ನು ತಪ್ಪಿಸಿ',
        'Minimize stress in the herd': 'ಮಂದೆಯಲ್ಲಿನ ಒತ್ತಡವನ್ನು ಕಡಿಮೆ ಮಾಡಿ',
        'Keep pesticides and chemical products locked away': 'ಕೀಟನಾಶಕಗಳು ಮತ್ತು ರಾಸಾಯನಿಕ ವಸ್ತುಗಳನ್ನು ಬೀಗದ ಅಡಿಯಲ್ಲಿ ಇರಿಸಿ',
        'Prevent access to toxic weeds or pasture areas': 'ವಿಷಕಾರಿ ಕಳೆಗಳು ಅಥವಾ ಹುಲ್ಲುಗಾವಲು ಪ್ರದೇಶಗಳಿಗೆ ಪ್ರವೇಶವನ್ನು ತಡೆಯಿರಿ',
        'Vaccinate against rabies where applicable': 'ಅನ್ವಯವಾಗುವಲ್ಲಿ ರೇಬೀಸ್ ವಿರುದ್ಧ ಲಸಿಕೆ ಹಾಕಿ',
        'Run regular fecal tests and deworm accordingly': 'ನಿಯಮಿತ ಮಲ ಪರೀಕ್ಷೆಗಳನ್ನು ನಡೆಸಿ ಮತ್ತು ಜಂತುನಾಶಕ ನೀಡಿ',
        'Provide feed with adequate protein and energy content': 'ಸಾಕಷ್ಟು ಪ್ರೋಟೀನ್ ಮತ್ತು ಶಕ್ತಿಯುಳ್ಳ ಆಹಾರವನ್ನು ಒದಗಿಸಿ',
        'Quarantine new stock to prevent wasting diseases': 'ರೋಗಗಳನ್ನು ತಡೆಗಟ್ಟಲು ಹೊಸ ಪ್ರಾಣಿಗಳನ್ನು ಕ್ವಾರಂಟೈನ್ ಮಾಡಿ',
        'Vaccinate goats with Tetanus Toxoid': 'ಮೇಕೆಗಳಿಗೆ ಧನುರ್ವಾಯು ಟಾಕ್ಸಾಯ್ಡ್ ಲಸಿಕೆ ಹಾಕಿ',
        'Disinfect all wounds and use sterile tools for castration/docking': 'ಎಲ್ಲಾ ಗಾಯಗಳನ್ನು ಸೋಂಕುರಹಿತಗೊಳಿಸಿ ಮತ್ತು ವಂಧೀಕರಿಸಿದ ಉಪಕರಣಗಳನ್ನು ಬಳಸಿ',
        'Ensure clean kidding environments': 'ಮರಿ ಹಾಕುವ ಪರಿಸರ ಸ್ವಚ್ಛವಾಗಿರಲಿ',
        'Avoid overcrowded, dusty, or drafty housing': 'ಕಿಕ್ಕಿರಿದ, ಧೂಳು ತುಂಬಿದ ಅಥವಾ ಗಾಳಿ ಇರುವ ವಸತಿಯನ್ನು ತಪ್ಪಿಸಿ',
        'Vaccinate against pasteurellosis': 'ಪಾಶ್ಚರೆಲೋಸಿಸ್ ವಿರುದ್ಧ ಲಸಿಕೆ ಹಾಕಿ',
        'Provide adequate ventilation in the shed': 'ಕೊಟ್ಟಿಗೆಯಲ್ಲಿ ಸಾಕಷ್ಟು ಗಾಳಿ ಸೌಕರ್ಯವನ್ನು ಒದಗಿಸಿ',
        'Avoid feeding moldy silage or sudden carbohydrate excess': 'ಬೂಷ್ಟು ಹಿಡಿದ ಸೈಲೇಜ್ ಅಥವಾ ಹಠಾತ್ ಕಾರ್ಬೋಹೈಡ್ರೇಟ್ ಅಧಿಕ ಆಹಾರವನ್ನು ತಪ್ಪಿಸಿ',
        'Maintain clean feed and water supply': 'ಸ್ವಚ್ಛ ಆಹಾರ ಮತ್ತು ನೀರಿನ ಸರಬರಾಜನ್ನು ನಿರ್ವಹಿಸಿ',
        'Provide mineral supplements containing thiamine': 'ಥಯಾಮಿನ್ ಹೊಂದಿರುವ ಖನಿಜ ಪೂರಕಗಳನ್ನು ಒದಗಿಸಿ',
        'Inspect pastures for toxic weeds and discard moldy feed': 'ವಿಷಕಾರಿ ಕಳೆಗಳಿಗಾಗಿ ಹುಲ್ಲುಗಾವಲುಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ ಮತ್ತು ಹಾಳಾದ ಮೇವನ್ನು ಬಿಸಾಡಿ',
        'Provide complete mineral block containing magnesium and calcium': 'ಮೆಗ್ನೀಸಿಯಮ್ ಮತ್ತು ಕ್ಯಾಲ್ಸಿಯಂ ಹೊಂದಿರುವ ಖನಿಜ ಬ್ಲಾಕ್ ಒದಗಿಸಿ',
        'Ensure shelter from extreme cold': 'ತೀವ್ರ ಚಳಿಯಿಂದ ರಕ್ಷಣೆ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ',
        'Provide adequate green fodder or silage': 'ಸಾಕಷ್ಟು ಹಸಿರು ಮೇವು ಅಥವಾ ಸೈಲೇಜ್ ಒದಗಿಸಿ',
        'Feed vitamin A supplements regularly during dry seasons': 'ಒಣ ಅವಧಿಯಲ್ಲಿ ನಿಯಮಿತವಾಗಿ ವಿಟಮಿನ್ ಎ ಪೂರಕಗಳನ್ನು ನೀಡಿ',
        'Ensure adequate nutrition for pregnant does': 'ಗರ್ಭಿಣಿ ಮೇಕೆಗಳಿಗೆ ಸಾಕಷ್ಟು ಪೋಷಣೆಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ',
        'Antibiotics (Penicillin/Streptomycin under vet advice)': 'ಆಂಟಿಬಯೋಟಿಕ್ಸ್ (ಪಶುವೈದ್ಯರ ಸಲಹೆಯ ಮೇರೆಗೆ ಪೆನ್ಸಿಲಿನ್/ಸ್ಟ್ರೆಪ್ಟೊಮೈಸಿನ್)',
        'Anti-inflammatory drugs': 'ಉರಿಯೂತ ನಿವಾರಕ ಔಷಧಗಳು',
        'Antispasmodics': 'ಸೆಳೆತ ನಿವಾರಕಗಳು',
        'Dewormers (if caused by parasites)': 'ಜಂತುನಾಶಕಗಳು (ಪರಾವಲಂಬಿಗಳಿಂದ ಉಂಟಾಗಿದ್ದರೆ)',
        'Carminative mixtures for gas relief': 'ಅನಿಲ ಪರಿಹಾರಕ್ಕಾಗಿ ಕಾರ್ಮಿನೇಟಿವ್ ಮಿಶ್ರಣಗಳು',
        'Multivitamin supplements': 'ಮಲ್ಟಿವಿಟಮಿನ್ ಪೂರಕಗಳು',
        'Supportive electrolytes': 'ಪೋಷಕ ವಿದ್ಯುದ್ವಿಭಜಕಗಳು (ಎಲೆಕ್ಟ್ರೋಲೈಟ್ಸ್)',
        'Antipyretics if fever is present': 'ಜ್ವರವಿದ್ದರೆ ಜ್ವರನಿವಾರಕಗಳು',
        'Calcium borogluconate (if metabolic)': 'ಕ್ಯಾಲ್ಸಿಯಂ ಬೊರೊಗ್ಲುಕೋನೇಟ್ (ಚಯಾಪಚಯ ದೋಷವಿದ್ದರೆ)',
        'Vitamin B-complex (especially Thiamine)': 'ವಿಟಮಿನ್ ಬಿ-ಕಾಂಪ್ಲೆಕ್ಸ್ (ವಿಶೇಷವಾಗಿ ಥಯಾಮಿನ್)',
        'Anti-inflammatories': 'ಉರಿಯೂತ ನಿವಾರಕಗಳು',
        'Rumen tonic/appetizers': 'ರುಮೆನ್ ಟಾನಿಕ್/ಹಸಿವು ಹೆಚ್ಚಿಸುವ ಔಷಧಗಳು',
        'Dewormers (if chronic)': 'ಜಂತುನಾಶಕಗಳು (ದೀರ್ಘಕಾಲದಾಗಿದ್ದರೆ)',
        'Atropine sulfate (antidote for organophosphate poisoning)': 'ಅಟ್ರೋಪಿನ್ ಸಲ್ಫೇಟ್ (ವಿಷಕ್ಕೆ ಪ್ರತಿವಿಷ)',
        'Activated charcoal': 'ಸಕ್ರಿಯ ಇದ್ದಿಲು (ಆಕ್ಟಿವೇಟೆಡ್ ಚಾರ್ಕೋಲ್)',
        'Anticonvulsants': 'ಸೆಳೆತ ನಿರೋಧಕಗಳು',
        'Broad-spectrum dewormers': 'ಬ್ರಾಡ್-ಸ್ಪೆಕ್ಟ್ರಮ್ ಜಂತುನಾಶಕಗಳು',
        'Protein concentrates': 'ಪ್ರೋಟೀನ್ ಸಾಂದ್ರೀಕರಣಗಳು',
        'Mineral supplements': 'ಖನಿಜ ಪೂರಕಗಳು',
        'Tetanus antitoxin': 'ಧನುರ್ವಾಯು ಆಂಟಿಟಾಕ್ಸಿನ್',
        'Penicillin/Antibiotics': 'ಪೆನ್ಸಿಲಿನ್/ಆಂಟಿಬಯೋಟಿಕ್ಸ್',
        'Muscle relaxants/Sedatives': 'ಸ್ನಾಯು ಸಡಿಲಗೊಳಿಸುವ ಔಷಧಗಳು/ಶಾಂತಗೊಳಿಸುವಿಕೆ',
        'Broad-spectrum antibiotics': 'ಬ್ರಾಡ್-ಸ್ಪೆಕ್ಟ್ರಮ್ ಆಂಟಿಬಯೋಟಿಕ್ಸ್',
        'Mucolytics/Expectorants': 'ಲೋಳೆ ಕರಗಿಸುವ/ಕೆಮ್ಮಿನ ನಿವಾರಕಗಳು',
        'Dewormers for nasal bots': 'ಮೂಗಿನ ನೊಣಗಳಿಗೆ ಜಂತುನಾಶಕ',
        'Thiamine (Vitamin B1) injections': 'ಥಯಾಮಿನ್ (ವಿಟಮಿನ್ ಬಿ1) ಚುಚ್ಚುಮದ್ದು',
        'High-dose antibiotics (e.g., penicillin for listeriosis)': 'ಹೆಚ್ಚಿನ ಪ್ರಮಾಣದ ಪ್ರತಿಜೀವಕಗಳು (ಪೆನ್ಸಿಲಿನ್)',
        'Corticosteroids': 'ಕಾರ್ಟಿಕೊಸ್ಟೆರಾಯ್ಡ್ಗಳು',
        'Magnesium sulfate / Calcium injections': 'ಮೆಗ್ನೀಸಿಯಮ್ ಸಲ್ಫೇಟ್ / ಕ್ಯಾಲ್ಸಿಯಂ ಚುಚ್ಚುಮದ್ದು',
        'Activated charcoal (if poisoning is suspected)': 'ಸಕ್ರಿಯ ಇದ್ದಿಲು (ವಿಷ ಶಂಕೆ ಇದ್ದರೆ)',
        'Vitamin B-complex': 'ವಿಟಮಿನ್ ಬಿ-ಕಾಂಪ್ಲೆಕ್ಸ್',
        'Vitamin A injections or oral supplements': 'ವಿಟಮಿನ್ ಎ ಚುಚ್ಚುಮದ್ದು ಅಥವಾ ಮೌಖಿಕ ಪೂರಕಗಳು',
        'Antibiotic eye ointments (if pink eye is present)': 'ಪ್ರತಿಜೀವಕ ಕಣ್ಣಿನ ಮುಲಾಮು (ಕಣ್ಣಿನ ಸೋಂಕಿದ್ದರೆ)',
        'Isolate the goat to ensure easy access to feed': 'ಆಹಾರಕ್ಕೆ ಸುಲಭ ಪ್ರವೇಶವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಲು ಮೇಕೆಯನ್ನು ಪ್ರತ್ಯೇಕಿಸಿ',
        'Provide soft, non-abrasive, easily chewable feed': 'ಮೃದುವಾದ, ಒರಟಲ್ಲದ, ಸುಲಭವಾಗಿ ಜಗಿಯಬಹುದಾದ ಆಹಾರವನ್ನು ನೀಡಿ',
        'Consult a veterinarian immediately': 'ತಕ್ಷಣ ಪಶುವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ',
        'Isolate the animal in a comfortable space': 'ಪ್ರಾಣಿಗಳನ್ನು ಆರಾಮದಾಯಕ ಜಾಗದಲ್ಲಿ ಪ್ರತ್ಯೇಕಿಸಿ',
        'Do not force-feed the goat': 'ಮೇಕೆಗೆ ಬಲವಂತವಾಗಿ ಆಹಾರ ನೀಡಬೇಡಿ',
        'Call a veterinarian immediately as colic can be fatal': 'ತಕ್ಷಣ ಪಶುವೈದ್ಯರನ್ನು ಕರೆಸಿ, ಹೊಟ್ಟೆನೋವು ಮಾರಣಾಂತಿಕವಾಗಬಹುದು',
        'Move the goat to a cool, shaded, well-ventilated area': 'ಮೇಕೆಯನ್ನು ತಂಪಾದ, ನೆರಳಿನ, ಗಾಳಿಯಾಡುವ ಜಾಗಕ್ಕೆ ಸರಿಸಿ',
        'Offer clean fresh water and electrolytes': 'ಸ್ವಚ್ಛವಾದ ತಾಜಾ ನೀರು ಮತ್ತು ಎಲೆಕ್ಟ್ರೋಲೈಟ್\u200cಗಳನ್ನು ನೀಡಿ',
        'Contact a veterinarian to diagnose the root cause': 'ಮೂಲ ಕಾರಣವನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಪಶುವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ',
        'Place the goat on thick, dry bedding to prevent sores': 'ಗಾಯಗಳನ್ನು ತಡೆಗಟ್ಟಲು ಮೇಕೆಯನ್ನು ದಪ್ಪನೆಯ ಒಣ ಹಾಸಿಗೆಯ ಮೇಲೆ ಇರಿಸಿ',
        'Provide food and water within easy reach': 'ಆಹಾರ ಮತ್ತು ನೀರನ್ನು ಸುಲಭವಾಗಿ ತಲುಪುವಂತೆ ಒದಗಿಸಿ',
        'Consult a vet for neurological or metabolic assessment': 'ನರರೋಗ ಅಥವಾ ಚಯಾಪಚಯ ಮೌಲ್ಯಮಾಪನಕ್ಕಾಗಿ ಪಶುವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ',
        'Isolate the goat to monitor its feed intake': 'ಆಹಾರ ಸೇವನೆಯನ್ನು ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡಲು ಮೇಕೆಯನ್ನು ಪ್ರತ್ಯೇಕಿಸಿ',
        'Offer fresh, highly palatable browse (leaves) or grass': 'ತಾಜಾ, ರುಚಿಕರವಾದ ಎಲೆಗಳು ಅಥವಾ ಹುಲ್ಲನ್ನು ನೀಡಿ',
        'Check body temperature for fever': 'ಜ್ವರಕ್ಕಾಗಿ ದೇಹದ ಉಷ್ಣತೆಯನ್ನು ಪರಿಶೀಲಿಸಿ',
        'Handle the goat carefully using protective gloves': 'ರಕ್ಷಣಾತ್ಮಕ ಕೈಗವಸುಗಳನ್ನು ಧರಿಸಿ ಮೇಕೆಯನ್ನು ಜಾಗರೂಕತೆಯಿಂದ ನಿಭಾಯಿಸಿ',
        'Check for visible blockages in the mouth without getting bitten': 'ಕಚ್ಚಿಸಿಕೊಳ್ಳದೆ ಬಾಯಿಯಲ್ಲಿ ಕಾಣಿಸುವ ಅಡಚಣೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ',
        'Provide the affected goat with high-quality, high-protein feed separately': 'ಬಾಧಿತ ಮೇಕೆಗೆ ಉತ್ತಮ ಗುಣಮಟ್ಟದ, ಹೆಚ್ಚಿನ ಪ್ರೋಟೀನ್ ಆಹಾರವನ್ನು ಪ್ರತ್ಯೇಕವಾಗಿ ಒದಗಿಸಿ',
        'Ensure the goat is not bullied by others during feeding': 'ಆಹಾರದ ಸಮಯದಲ್ಲಿ ಮೇಕೆಯನ್ನು ಇತರ ಪ್ರಾಣಿಗಳು ಹಿಂಸಿಸದಂತೆ ನೋಡಿಕೊಳ್ಳಿ',
        'Get a veterinary evaluation for chronic diseases': 'ದೀರ್ಘಕಾಲದ ಕಾಯಿಲೆಗಳಿಗಾಗಿ ಪಶುವೈದ್ಯಕೀಯ ಮೌಲ್ಯಮಾಪನ ಪಡೆಯಿರಿ',
        'Place the goat in a quiet, dark, and deeply bedded stall to avoid spasms': 'ಸೆಳೆತವನ್ನು ತಪ್ಪಿಸಲು ಮೇಕೆಯನ್ನು ಶಾಂತ, ಕತ್ತಲೆಯಾದ ಒಣ ಹಾಸಿಗೆಯ ಕೊಟ್ಟಿಗೆಯಲ್ಲಿ ಇರಿಸಿ',
        'Keep food and water at chest level': 'ಆಹಾರ ಮತ್ತು ನೀರನ್ನು ಎದೆಯ ಮಟ್ಟದಲ್ಲಿ ಇರಿಸಿ',
        'Call a vet urgently': 'ತಕ್ಷಣ ಪಶುವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ',
        'Isolate the goat to prevent spreading respiratory droplets': 'ಉಸಿರಾಟದ ಹನಿಗಳು ಹರಡುವುದನ್ನು ತಡೆಗಟ್ಟಲು ಮೇಕೆಯನ್ನು ಪ್ರತ್ಯೇಕಿಸಿ',
        'Keep the animal warm, dry, and sheltered': 'ಪ್ರಾಣಿಗಳನ್ನು ಬೆಚ್ಚಗೆ, ಒಣದಾಗಿ ಮತ್ತು ಆಶ್ರಯದಲ್ಲಿ ಇರಿಸಿ',
        'Clean the nostrils with a soft damp cloth': 'ಮೃದುವಾದ ಒದ್ದೆ ಬಟ್ಟೆಯಿಂದ ಮೂಗಿನ ಹೊಳ್ಳೆಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ',
        'Isolate in a safe, padded stall to prevent injury from circling/falling': 'ಸುತ್ತು ಬರುವುದು/ಬೀಳುವುದರಿಂದ ಗಾಯವಾಗುವುದನ್ನು ತಪ್ಪಿಸಲು ಸುರಕ್ಷಿತ ಜಾಗದಲ್ಲಿ ಪ್ರತ್ಯೇಕಿಸಿ',
        'Support the head if the goat is unable to lift it': 'ಮೇಕೆಗೆ ತಲೆ ಎತ್ತಲು ಸಾಧ್ಯವಾಗದಿದ್ದರೆ ತಲೆಗೆ ಆಸರೆ ನೀಡಿ',
        'Seek urgent vet care': 'ತುರ್ತು ಪಶುವೈದ್ಯಕೀಯ ಆರೈಕೆಯನ್ನು ಪಡೆಯಿರಿ',
        'Move the goat to a warm, quiet, stress-free shelter': 'ಮೇಕೆಯನ್ನು ಬೆಚ್ಚಗಿನ, ಶಾಂತ, ಒತ್ತಡವಿಲ್ಲದ ಆಶ್ರಯಕ್ಕೆ ಸರಿಸಿ',
        'Prevent self-injury by removing sharp objects': 'ತೀಕ್ಷ್ಣವಾದ ವಸ್ತುಗಳನ್ನು ತೆಗೆದುಹಾಕುವ ಮೂಲಕ ಸ್ವಯಂ ಗಾಯವನ್ನು ತಡೆಯಿರಿ',
        'Call a veterinarian immediately': 'ತಕ್ಷಣ ಪಶುವೈದ್ಯರನ್ನು ಕರೆಸಿ',
        'Keep the blind goat in a safe, familiar pen before sunset': 'ಸೂರ್ಯಾಸ್ತದ ಮೊದಲು ಕುರುಡು ಮೇಕೆಯನ್ನು ಸುರಕ್ಷಿತ, ಪರಿಚಿತ ಪೆನ್ನಿನಲ್ಲಿ ಇರಿಸಿ',
        'Provide easily accessible feed and water': 'ಸುಲಭವಾಗಿ ಪ್ರವೇಶಿಸಬಹುದಾದ ಆಹಾರ ಮತ್ತು ನೀರನ್ನು ಒದಗಿಸಿ',
        'Consult a vet for nutritional support': 'ಪೌಷ್ಟಿಕಾಂಶದ ಬೆಂಬಲಕ್ಕಾಗಿ ಪಶುವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸಿ',
        'Soft green leaves, browse, and wet mash or gruel': 'ಮೃದುವಾದ ಹಸಿರು ಎಲೆಗಳು, ಮೇವು ಮತ್ತು ಒದ್ದೆಯಾದ ದಂಟು',
        'Ensure clean drinking water with electrolyte support': 'ಎಲೆಕ್ಟ್ರೋಲೈಟ್ ಬೆಂಬಲದೊಂದಿಗೆ ಸ್ವಚ್ಛ ಕುಡಿಯುವ ನೀರನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ',
        'Fresh green leaves, high-quality hay': 'ತಾಜಾ ಹಸಿರು ಎಲೆಗಳು, ಉತ್ತಮ ಗುಣಮಟ್ಟದ ಒಣ ಹುಲ್ಲು',
        'Provide fresh, clean water': 'ತಾಜಾ, ಸ್ವಚ್ಛ ನೀರನ್ನು ಒದಗಿಸಿ',
        'High-energy digestible feed, green browse': 'ಹೆಚ್ಚಿನ ಶಕ್ತಿಯ ಸುಲಭವಾಗಿ ಜೀರ್ಣವಾಗುವ ಆಹಾರ, ಹಸಿರು ಸೊಪ್ಪು',
        'Clean water with electrolytes': 'ಎಲೆಕ್ಟ್ರೋಲೈಟ್\u200cಗಳೊಂದಿಗೆ ಸ್ವಚ್ಛ ನೀರು',
        'Legume hay, fresh browse': 'ಫಲಿ ಪದಾರ್ಥದ ಒಣ ಹುಲ್ಲು, ತಾಜಾ ಸೊಪ್ಪು',
        'Keep fresh water close to the animal': 'ಪ್ರಾಣಿಗಳ ಹತ್ತಿರ ಸ್ವಚ್ಛ ನೀರನ್ನು ಇಡಿ',
        'Palatable leaves (like mulberry or jackfruit leaves)': 'ರುಚಿಕರವಾದ ಎಲೆಗಳು (ಹಿಪ್ಪನೇರಳೆ ಅಥವಾ ಹಲಸಿನ ಎಲೆಗಳು)',
        'Ensure clean drinking water': 'ಸ್ವಚ್ಛ ಕುಡಿಯುವ ನೀರನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ',
        'Withhold food initially until veterinarian examines': 'ಪಶುವೈದ್ಯರು ಪರೀಕ್ಷಿಸುವವರೆಗೆ ಆರಂಭದಲ್ಲಿ ಆಹಾರ ನೀಡಬೇಡಿ',
        'Provide clean water if goat is stable and able to swallow': 'ಮೇಕೆ ಸ್ಥಿರವಾಗಿದ್ದರೆ ಮತ್ತು ನುಂಗಲು ಸಾಧ್ಯವಾದರೆ ಸ್ವಚ್ಛ ನೀರನ್ನು ನೀಡಿ',
        'Leguminous fodder, concentrate feed': 'ದ್ವಿದಳ ಧಾನ್ಯದ ಮೇವು, ಸಾಂದ್ರೀಕೃತ ಮೇವು',
        'Mineral block supplementation': 'ಖನಿಜ ಬ್ಲಾಕ್ ಪೂರಕ',
        'Easy-to-swallow soft feed or gruel': 'ನುಂಗಲು ಸುಲಭವಾದ ಮೃದುವಾದ ಆಹಾರ ಅಥವಾ ಗಂಜಿ',
        'Keep fresh water close to chest level': 'ಎದೆಯ ಮಟ್ಟದ ಹತ್ತಿರ ಸ್ವಚ್ಛ ನೀರನ್ನು ಇಡಿ',
        'Dust-free high-quality green browse': 'ಧೂಳು ಮುಕ್ತ ಉತ್ತಮ ಗುಣಮಟ್ಟದ ಹಸಿರು ಸೊಪ್ಪು',
        'Offer fresh palatable feed and support while feeding if needed': 'ಅಗತ್ಯವಿದ್ದರೆ ತಾಜಾ ರುಚಿಕರವಾದ ಆಹಾರವನ್ನು ನೀಡಿ ಮತ್ತು ಆಹಾರದ ಸಮಯದಲ್ಲಿ ಬೆಂಬಲಿಸಿ',
        'Provide water close to head level': 'ತಲೆಯ ಮಟ್ಟದ ಹತ್ತಿರ ನೀರನ್ನು ಒದಗಿಸಿ',
        'Provide clean, fresh water and soft green grass': 'ಸ್ವಚ್ಛವಾದ, ತಾಜಾ ನೀರು ಮತ್ತು ಮೃದುವಾದ ಹಸಿರು ಹುಲ್ಲನ್ನು ನೀಡಿ',
        'Mineral mixtures containing magnesium': 'ಮೆಗ್ನೀಸಿಯಮ್ ಹೊಂದಿರುವ ಖನಿಜ ಮಿಶ್ರಣಗಳು',
        'Fresh green leaves, carrots, high-quality grass hay': 'ತಾಜಾ ಹಸಿರು ಎಲೆಗಳು, ಕ್ಯಾರೆಟ್, ಉತ್ತಮ ಗುಣಮಟ್ಟದ ಹುಲ್ಲು',
        'Mineral and vitamin mix': 'ಖನಿಜ ಮತ್ತು ವಿಟಮಿನ್ ಮಿಶ್ರಣ',
        'Clean feeding troughs to prevent bacterial buildup': 'ಬ್ಯಾಕ್ಟೀರಿಯಾದ ಬೆಳವಣಿಗೆಯನ್ನು ತಡೆಯಲು ಮೇವು ತಿನ್ನುವ ತೊಟ್ಟಿಗಳನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ',
        'Sanitize any equipment used to inspect the mouth': 'ಬಾಯಿಯನ್ನು ಪರೀಕ್ಷಿಸಲು ಬಳಸುವ ಯಾವುದೇ ಉಪಕರಣವನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ',
        'Keep the goat shelter clean and dry': 'ಮೇಕೆ ಆಶ್ರಯವನ್ನು ಸ್ವಚ್ಛ ಮತ್ತು ಒಣದಾಗಿ ಇಡಿ',
        'Sanitize feeding troughs regularly': 'ಮೇವು ತಿನ್ನುವ ತೊಟ್ಟಿಗಳನ್ನು ನಿಯಮಿತವಾಗಿ ಸ್ವಚ್ಛಗೊಳಿಸಿ',
        'Maintain dry bedding to prevent secondary infections': 'ಸೆಕೆಂಡರಿ ಸೋಂಕುಗಳನ್ನು ತಡೆಯಲು ಹಾಸಿಗೆ ಒಣದಾಗಿ ಇಡಿ',
        'Provide adequate ventilation in the housing': 'ವಸತಿಯಲ್ಲಿ ಸಾಕಷ್ಟು ಗಾಳಿ ಸೌಕರ್ಯವನ್ನು ಒದಗಿಸಿ',
        'Ensure soft and dry flooring to prevent foot rot or joint injuries': 'ಕಾಲು ಕೊಳೆತ ಅಥವಾ ಕೀಲು ಗಾಯಗಳನ್ನು ತಡೆಯಲು ಮೃದುವಾದ ಮತ್ತು ಒಣ ನೆಲವನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ',
        'Clean the pen floor regularly': 'ಪೆನ್ ನೆಲವನ್ನು ನಿಯಮಿತವಾಗಿ ಸ್ವಚ್ಛಗೊಳಿಸಿ',
        'Remove uneaten wet feed to prevent mold growth': 'ಬೂಷ್ಟು ಬೆಳೆಯುವುದನ್ನು ತಡೆಯಲು ತಿನ್ನದ ಒದ್ದೆಯಾದ ಆಹಾರವನ್ನು ತೆಗೆದುಹಾಕಿ',
        'Maintain overall cleanliness of feeding zones': 'ಆಹಾರ ವಲಯಗಳ ಒಟ್ಟಾರೆ ಶುಚಿತ್ವವನ್ನು ನಿರ್ವಹಿಸಿ',
        'Wear gloves when handling foaming goats (zoonotic rabies risk)': 'ನೊರೆ ಬರುವ ಮೇಕೆಗಳನ್ನು ನಿರ್ವಹಿಸುವಾಗ ಕೈಗವಸುಗಳನ್ನು ಧರಿಸಿ',
        'Disinfect the area and isolate the goat immediately': 'ಪ್ರದೇಶವನ್ನು ಸೋಂಕುರಹಿತಗೊಳಿಸಿ ಮತ್ತು ಮೇಕೆಯನ್ನು ತಕ್ಷಣ ಪ್ರತ್ಯೇಕಿಸಿ',
        'Maintain pasture rotation to prevent worm reinfection': 'ಹುಳುಗಳ ಮರು-ಸೋಂಕನ್ನು ತಡೆಯಲು ಹುಲ್ಲುಗಾವಲು ತಿರುಗುವಿಕೆಯನ್ನು ನಿರ್ವಹಿಸಿ',
        'Disinfect the quarantine area regularly': 'ಕ್ವಾರಂಟೈನ್ ಪ್ರದೇಶವನ್ನು ನಿಯಮಿತವಾಗಿ ಸೋಂಕುರಹಿತಗೊಳಿಸಿ',
        'Perform surgeries in dry, clean, and sterilized areas': 'ಒಣ, ಸ್ವಚ್ಛ ಮತ್ತು ಕ್ರಿಮಿಶುದ್ಧೀಕರಿಸಿದ ಪ್ರದೇಶಗಳಲ್ಲಿ ಶಸ್ತ್ರಚಿಕಿತ್ಸೆಗಳನ್ನು ನಡೆಸಿ',
        'Ensure deep, clean straw bedding': 'ದಟ್ಟವಾದ, ಸ್ವಚ್ಛವಾದ ಹುಲ್ಲು ಹಾಸಿಗೆಯನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ',
        'Ventilate the shed properly to reduce ammonia buildup': 'ಅಮೋನಿಯಾ ಶೇಖರಣೆಯನ್ನು ಕಡಿಮೆ ಮಾಡಲು ಕೊಟ್ಟಿಗೆಯನ್ನು ಸರಿಯಾಗಿ ಗಾಳಿ ಮಾಡಿ',
        'Clean the housing area daily': 'ವಸತಿ ಪ್ರದೇಶವನ್ನು ಪ್ರತಿದಿನ ಸ್ವಚ್ಛಗೊಳಿಸಿ',
        'Avoid feeding spoiled or poorly fermented silage': 'ಹಾಳಾದ ಸೈಲೇಜ್ ನೀಡುವುದನ್ನು ತಪ್ಪಿಸಿ',
        'Ensure clean and sanitized troughs': 'ಸ್ವಚ್ಛ ಮತ್ತು ನೈರ್ಮಲ್ಯದ ಮೇವಿನ ತೊಟ್ಟಿಗಳನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ',
        'Keep bedding clean, soft, and dry': 'ಹಾಸಿಗೆಯನ್ನು ಸ್ವಚ್ಛವಾಗಿ, ಮೃದುವಾಗಿ ಮತ್ತು ಒಣದಾಗಿ ಇಡಿ',
        'Isolate in a peaceful, noise-free area': 'ಶಾಂತಿಯುತ, ಶಬ್ದ ಮುಕ್ತ ಪ್ರದೇಶದಲ್ಲಿ ಪ್ರತ್ಯೇಕಿಸಿ',
        "Remove obstacles from the blind goat's living space": 'ಕುರುಡು ಮೇಕೆಯ ವಾಸಸ್ಥಳದಿಂದ ಅಡೆತಡೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ',
        'Maintain clean housing to prevent eye flies or irritants': 'ಕಣ್ಣಿನ ನೊಣಗಳು ಅಥವಾ ಕಿರಿಕಿರಿಯುಂಟುಮಾಡುವ ಅಂಶಗಳನ್ನು ತಡೆಯಲು ಸ್ವಚ್ಛ ವಸತಿ ನಿರ್ವಹಿಸಿ',
    },
    "hi": {
        'low': 'कम',
        'moderate': 'मध्यम',
        'high': 'उच्च',
        'critical': 'गंभीर',
        'emergency_alert': 'आपातकालीन पशु चिकित्सा ध्यान आवश्यक है: यह बीमारी गंभीर है। तुरंत पशु को अलग करें और पशु चिकित्सा डॉक्टर से संपर्क करें।',
        'Healthy': 'स्वस्थ',
        'Foot and Mouth Disease': 'खुरपका और मुंहपका रोग',
        'Lumpy Skin Disease': 'ढेलादार त्वचा रोग (लम्पी)',
        'Mastitis': 'थनैला रोग',
        'Bloat (Ruminal Tympany)': 'अफरा रोग (पेट फूलना)',
        'Black Quarter (Black Leg)': 'लंगड़ा बुखार',
        'Peste des Petits Ruminants (PPR)': 'पीपीआर रोग (बकरी प्लेग)',
        'Goat Pox': 'बकरी चेचक',
        'Contagious Ecthyma (Orf)': 'संक्रामक एक्थीमा (ओर्फ)',
        'Enterotoxemia': 'आंत्रविषैलापन (फड़किया)',
        'Foot Rot': 'खुर सड़न',
        'Sheep Scab (Psoroptic Mange)': 'भेड़ की खुजली',
        'Blue Tongue': 'नीली जीभ रोग',
        'Pneumonia': 'निमोनिया',
        'The animal is in excellent health due to proper care, good hygiene, and a well-balanced diet.': 'उचित देखभाल, अच्छी स्वच्छता और संतुलित आहार के कारण पशु उत्कृष्ट स्वास्थ्य में है।',
        'The goat is healthy because of proper herd management, good pasture access, and adequate parasite control.': 'उचित झुंड प्रबंधन, अच्छे चरागाह और पर्याप्त परजीवी नियंत्रण के कारण बकरी स्वस्थ है।',
        'The sheep is in optimal health due to good grazing management, effective parasite control, and proper flock care.': 'अच्छे चराई प्रबंधन, प्रभावी परजीवी नियंत्रण और उचित झुंड देखभाल के कारण भेड़ इष्टतम स्वास्थ्य में है।',
        'Clear eyes and alert posture': 'साफ आंखें और सतर्क मुद्रा',
        'Smooth and shiny coat': 'चिकनी और चमकदार त्वचा',
        'Normal breathing and appetite': 'सामान्य सांस और भूख',
        'Normal chewing of cud': 'सामान्य जुगाली करना',
        'No visible lesions or swelling': 'कोई स्पष्ट घाव या सूजन नहीं',
        'Active and alert behavior': 'सक्रिय और सतर्क व्यवहार',
        'Normal body temperature (39°C)': 'सामान्य शरीर का तापमान (39°C)',
        'Firm, pelleted feces': 'कड़ी, गोलियों जैसी लीद',
        'Normal appetite and rumination': 'सामान्य भूख और जुगाली',
        'Shiny, smooth coat': 'चमकदार, चिकनी त्वचा',
        'Staying with the flock (not isolated)': 'झुंड के साथ रहना (अलग नहीं)',
        'Alert and responsive': 'सतर्क और संवेदनशील',
        'Normal breathing rate': 'सामान्य श्वसन दर',
        'Good wool condition without patches': 'पैच के बिना ऊन की अच्छी स्थिति',
        'Even gait without limping': 'बिना लंगड़ाए सामान्य चाल',
        'Good nutrition and balanced diet': 'अच्छा पोषण और संतुलित आहार',
        'Proper vaccination schedule': 'उचित टीकाकरण कार्यक्रम',
        'Clean and hygienic environment': 'साफ और स्वच्छ वातावरण',
        'Low stress levels': 'कम तनाव का स्तर',
        'Excellent farm management': 'उत्कृष्ट फार्म प्रबंधन',
        'Timely vaccination and deworming': 'समय पर टीकाकरण और कृमिनाशक देना',
        'Nutritious browse and pasture': 'पौष्टिक चारा और चरागाह',
        'Clean and dry housing': 'साफ और सूखा आवास',
        'Optimal flock management': 'इष्टतम झुंड प्रबंधन',
        'Good nutrition and pasture quality': 'अच्छा पोषण और चरागाह की गुणवत्ता',
        'Effective parasite control program': 'प्रभावी परजीवी नियंत्रण कार्यक्रम',
        'Low stress environment': 'कम तनाव वाला वातावरण',
        'Continue regular health checkups': 'नियमित स्वास्थ्य जांच जारी रखें',
        'Maintain current feeding schedule': 'वर्तमान भोजन कार्यक्रम बनाए रखें',
        'Keep up with seasonal vaccinations': 'मौसमी टीकाकरण कराते रहें',
        'Ensure access to clean water': 'साफ पानी की उपलब्धता सुनिश्चित करें',
        'Maintain regular deworming schedule': 'नियमित कृमिनाशक कार्यक्रम बनाए रखें',
        'Continue annual vaccinations': 'वार्षिक टीकाकरण जारी रखें',
        'Provide adequate shelter from extreme weather': 'खराब मौसम से पर्याप्त सुरक्षा प्रदान करें',
        'Trim hooves regularly': 'नियमित रूप से खुरों की छंटाई करें',
        'Continue routine hoof trimming': 'नियमित रूप से खुरों को ट्रिम करना जारी रखें',
        'Maintain regular shearing schedule': 'नियमित रूप से बाल काटने (ऊन उतारने) का कार्यक्रम रखें',
        'Follow flock vaccination protocols': 'झुंड टीकाकरण नियमों का पालन करें',
        'Monitor pasture quality': 'चरागाह की गुणवत्ता की निगरानी करें',
        'No medicine required': 'किसी दवा की आवश्यकता नहीं है',
        'Routine deworming (every 3-6 months)': 'नियमित कृमिनाशक (हर 3-6 महीने में)',
        'Calcium supplements (if lactating)': 'कैल्शियम सप्लीमेंट (यदि दूध दे रही हो)',
        'Mineral mixture (50g daily)': 'खनिज मिश्रण (50 ग्राम दैनिक)',
        'No medicine needed': 'किसी दवा की आवश्यकता नहीं है',
        'Routine anthelmintics (deworming)': 'नियमित कृमिनाशक दवाएं',
        'Vitamin supplements during stress/pregnancy': 'तनाव/गर्भावस्था के दौरान विटामिन सप्लीमेंट',
        'Copper and zinc supplements if deficient': 'कमी होने पर तांबा और जस्ता सप्लीमेंट',
        'No medicine necessary': 'किसी दवा की आवश्यकता नहीं है',
        'Routine deworming based on fecal egg counts': 'गोबर परीक्षण के आधार पर नियमित कृमिनाशक',
        'Trace mineral supplements (ensure low copper)': 'खनिज सप्लीमेंट (कम तांबा सुनिश्चित करें)',
        'Vitamin E / Selenium if in deficient area': 'कमी वाले क्षेत्र में विटामिन ई / सेलेनियम',
        'Not applicable': 'लागू नहीं',
        'Monitor daily for any changes': 'दैनिक स्तर पर किसी भी बदलाव की निगरानी करें',
        'Maintain herd records': 'झुंड का रिकॉर्ड बनाए रखें',
        'Keep emergency vet contact handy': 'आपातकालीन पशु चिकित्सक का संपर्क पास रखें',
        'Regularly check for ticks or lice': 'नियमित रूप से किलनी या जुओं की जांच करें',
        'Monitor body condition score': 'शारीरिक स्थिति के स्कोर की निगरानी करें',
        'Check hooves for overgrowth': 'खुरों की अत्यधिक वृद्धि की जांच करें',
        'Perform regular body condition scoring': 'नियमित शारीरिक स्थिति स्कोरिंग करें',
        'Check for flystrike during warm months': 'गर्म महीनों में मक्खियों के प्रकोप (फ्लाईस्ट्राइक) की जांच करें',
        'Monitor lambing ewes closely': 'बच्चे देने वाली भेड़ों की बाहरीकी से निगरानी करें',
        'Balanced ratio of green and dry fodder': 'हरे और सूखे चारे का संतुलित अनुपात',
        'Concentrate feed based on milk yield': 'दूध की मात्रा के आधार पर संतुलित आहार',
        'Access to fresh, clean drinking water': 'ताजे और साफ पीने के पानी की उपलब्धता',
        'Provide salt licks': 'नमक चाटने के ब्लॉक (सॉल्ट लिक) प्रदान करें',
        'Access to varied browse (shrubs/leaves)': 'विभिन्न प्रकार की झाड़ियों/पत्तियों का चारा',
        'High-quality grass hay': 'उच्च गुणवत्ता वाली सूखी घास',
        'Loose goat-specific minerals': 'बकरियों के लिए खनिज मिश्रण',
        'Clean, fresh water always': 'हमेशा साफ और ताजा पानी',
        'High quality pasture grazing': 'उच्च गुणवत्ता वाले चरागाह में चराई',
        'Supplemental hay during winter/drought': 'सर्दियों/सूखे के दौरान अतिरिक्त घास',
        'Sheep-specific mineral mix (no added copper)': 'भेड़ों के लिए खनिज मिश्रण (बिना तांबे के)',
        'Fresh, unfrozen water access': 'ताजे पानी की उपलब्धता',
        'Daily cleaning of the shed': 'बाड़े की रोजाना सफाई',
        'Proper disposal of dung': 'गोबर का उचित निपटान',
        'Regular grooming/brushing of the cow': 'गाय की नियमित ग्रूमिंग/ब्रशिंग',
        'Maintain dry and comfortable bedding': 'सूखा और आरामदायक बिछौना बनाए रखें',
        'Keep pens dry and well-ventilated': 'बाड़ों को सूखा और हवादार रखें',
        'Clean water troughs daily': 'पानी की हौदियों को रोजाना साफ करें',
        'Disinfect kidding pens before use': 'उपयोग से पहले प्रसव बाड़ों को कीटाणुरहित करें',
        'Manage pasture rotation to reduce parasites': 'परजीवियों को कम करने के लिए चरागाह रोटेशन प्रबंधित करें',
        'Keep housing well-ventilated and dry': 'आवास को हवादार और सूखा रखें',
        'Provide clean, dry bedding': 'साफ और सूखा बिछौना प्रदान करें',
        'Use footbaths routinely to prevent hoof issues': 'खुर की समस्याओं से बचने के लिए नियमित रूप से फुटबाथ का उपयोग करें',
        'Shear before hot weather to prevent heat stress': 'गर्मी के तनाव से बचने के लिए गर्म मौसम से पहले ऊन उतारें',
        'Jaw Swelling': 'मैंडिबल में सूजन',
        'Kicking at Abdomen': 'पेट पर लात मारना',
        'Lethargy Syndrome': 'सुस्ती सिंड्रोम',
        'Limb Weakness': 'पैरों की कमजोरी',
        'Loss of Appetite': 'भूख न लगना',
        'Mouth Foaming': 'मुंह से झाग आना',
        'Muscle Atrophy': 'मांसपेशियों का क्षय',
        'Muscle Rigidity': 'मांसपेशियों में अकड़न',
        'Nasal Discharge': 'नाक से स्राव',
        'Neck Rigidity': 'गर्दन में अकड़न',
        'Nervous Tremors': 'तंत्रिका कंपन',
        'Night Blindness': 'रतौंधी',
        'Enlargement of jaw region': 'जबड़े के क्षेत्र का बढ़ना',
        'Pain while chewing': 'चबाते समय दर्द',
        'Signs of abdominal pain and discomfort': 'पेट दर्द और बेचैनी के लक्षण',
        'Restlessness': 'बेचैनी',
        'Lying down and getting up frequently': 'बार-बार बैठना और खड़ा होना',
        'Extreme tiredness': 'अत्यधिक थकान',
        'Reduced activity': 'कम गतिविधि',
        'Reluctance to move or stand': 'हिलने-डुलने या खड़े होने में आनाकानी',
        'Difficulty standing or walking': 'खड़े होने या चलने में कठिनाई',
        'Incoordination': 'असंतुलन',
        'Stumbling or weakness in legs': 'पैरों में लड़खड़ाहट या कमजोरी',
        'Reduced or no feed intake': 'चारा खाने में कमी या बंद होना',
        'Dullness': 'सुस्ती',
        'Reduced rumination': 'कम जुगाली करना',
        'Frothy saliva around mouth': 'मुंह के आसपास झागदार लार',
        'Excessive salivation': 'अत्यधिक लार बहना',
        'Choking signs': 'दम घुटने के लक्षण',
        'Loss of muscle mass over time': 'समय के साथ मांसपेशियों का कम होना',
        'Weight loss': 'वजन कम होना',
        'Visible bony prominences': 'दिखने वाली हड्डियां',
        'Stiff and tight muscles': 'कड़ी और तंग मांसपेशियां',
        'Sawhorse stance': 'लकड़ी के घोड़े जैसी मुद्रा',
        'Difficulty bending limbs or neck': 'अंगों या गर्दन को मोड़ने में कठिनाई',
        'Mucus or pus coming from nostrils': 'नथुनों से बलगम या मवाद आना',
        'Sneezing': 'छींक आना',
        'Coughing': 'खांसी',
        'Difficulty moving neck freely': 'गर्दन को स्वतंत्र रूप से हिलाने में कठिनाई',
        'Stiff neck (torticollis)': 'कड़ी गर्दन (टॉर्टिकॉलिस)',
        'Star-gazing posture': 'आसमान की ओर देखने जैसी मुद्रा',
        'Involuntary shaking movements': 'अनैच्छिक कंपन',
        'Muscle twitching': 'मांसपेशियों का फड़कना',
        'Shivering-like motions': 'कंपकंपी जैसी हरकतें',
        'Poor vision in low light': 'कम रोशनी में धुंधला दिखना',
        'Bumping into objects at dusk': 'शाम के समय चीजों से टकराना',
        'Dilated pupils that react slowly': 'पुतलियों का फैलना और धीमी प्रतिक्रिया',
        'Coarse or abrasive feed injuring oral cavity': 'मोटा या खुरदरा चारा मुंह में चोट पहुँचाता है',
        'Bacterial infection (e.g., Actinomyces/lumpy jaw)': 'बैक्टीरिया का संक्रमण (जैसे, एक्टिनोमाइसेस/लम्पी जॉ)',
        'Dental issues or tooth root abscess': 'दांतों की समस्याएं या दांतों की जड़ में फोड़ा',
        'Ruminal impaction or severe bloat': 'रुमेन में भोजन का फंसना या गंभीर पेट फूलना',
        'Gastrointestinal parasites': 'आंतों के परजीवी',
        'Ingestion of toxic plants or foreign objects': 'जहरीले पौधों या बाहरी वस्तुओं का सेवन',
        'Systemic infection or chronic disease': 'प्रणालीगत संक्रमण या पुरानी बीमारी',
        'Nutritional deficiencies': 'पोषक तत्वों की कमी',
        'Severe heat stress or dehydration': 'गंभीर गर्मी का तनाव या निर्जलीकरण',
        'Metabolic imbalances (e.g., calcium/magnesium deficiency)': 'चयापचय असंतुलन (जैसे, कैल्शियम/मैग्नीशियम की कमी)',
        'Neurological disorders or spinal injury': 'न्यूरोलॉजिकल विकार या रीढ़ की हड्डी में चोट',
        'Infectious arthritis or joint ill': 'संक्रामक गठिया या जोड़ों का रोग',
        'Fever or underlying infectious disease': 'बुखार या अंतर्निहित संक्रामक रोग',
        'Rumen acidosis or digestive upset': 'रुमेन एसिडोसिस या अपच',
        'Stress or dental pain': 'तनाव या दांत दर्द',
        'Ingestion of organophosphate pesticides or toxic plants': 'ऑर्गेनोफॉस्फेट कीटनाशकों या जहरीले पौधों का सेवन',
        'Rabies or other neurological infections': 'रेबीज या अन्य न्यूरोलॉजिकल संक्रमण',
        'Esophageal obstruction (choking)': 'ग्रासनली में रुकावट (दम घुटना)',
        'Chronic internal parasitism (worms/flukes)': 'पुरानी आंतरिक परजीवीता (कीड़े/फ्लूक)',
        'Malnutrition or protein deficiency': 'कुपोषण या प्रोटीन की कमी',
        "Chronic debilitating diseases (like Johne's disease)": 'लंबे समय तक कमजोर करने वाली बीमारियां (जैसे जोहने की बीमारी)',
        'Tetanus (Clostridium tetani infection)': 'टिटनेस (क्लोस्ट्रिडियम टेटानी संक्रमण)',
        'Strychnine poisoning or toxic plant ingestion': 'स्ट्राइकिन जहर या जहरीले पौधे का सेवन',
        'Severe electrolyte imbalance': 'गंभीर इलेक्ट्रोलाइट असंतुलन',
        'Respiratory tract infections (pasteurellosis/pneumonia)': 'श्वसन तंत्र के संक्रमण (पाश्चरेलोसिस/निमोनिया)',
        'Nasal bot infestation (Oestrus ovis)': 'नाक के बोट का संक्रमण (ओएस्ट्रस ओविस)',
        'Dusty or poorly ventilated housing': 'धूल भरा या हवादार आवास की कमी',
        'Polioencephalomalacia (PEM / Thiamine deficiency)': 'पोलियोएन्सेफालोमैलेशिया (पीईएम / थायमिन की कमी)',
        'Listeriosis (circling disease)': 'लिस्टेरियोसिस (चक्करदार बीमारी)',
        'Meningitis or spinal trauma': 'मेनिन्जाइटिस या रीढ़ की हड्डी का आघात',
        'Neurological toxicities (mycotoxins/poisonous plants)': 'न्यूरोलॉजिकल विषाक्तता (माइकोटॉक्सिन/जहरीले पौधे)',
        'Metabolic disorders (hypomagnesemia/hypocalcemia)': 'चयापचय संबंधी विकार (हाइपोमैग्नेसीमिया/हाइपोकैल्सीमिया)',
        'Infectious encephalitic diseases': 'संक्रामक एन्सेफलाइटिस बीमारियां',
        'Vitamin A deficiency': 'विटामिन ए की कमी',
        'Infectious keratoconjunctivitis (pink eye)': 'संक्रामक केराटोकोंजक्टिवाइटिस (आंख आना)',
        'Congenital eye defects': 'जन्मजात आंखों के दोष',
        'The goat developed jaw swelling due to a bacterial infection entering through a scratch in the mouth or a dental injury.': 'बकरी के जबड़े में सूजन मुंह में खरोंच या दांत की चोट के माध्यम से बैक्टीरिया के प्रवेश के कारण हुई।',
        'The goat is showing signs of severe colic or abdominal distress, which could be due to gas accumulation, impaction, or parasitic infection.': 'बकरी गंभीर पेट दर्द या पेट की परेशानी के लक्षण दिखा रही है, जो गैस संचय, भोजन फंसने या परजीवी संक्रमण के कारण हो सकता है।',
        'The goat is experiencing extreme tiredness and reduced activity, indicating an underlying systemic infection, metabolic issue, or high fever.': 'बकरी अत्यधिक थकान और कम गतिविधि का अनुभव कर रही है, जो एक अंतर्निहित प्रणालीगत संक्रमण, चयापचय समस्या या तेज बुखार का संकेत देती है।',
        'The goat has difficulty standing or walking due to muscle weakness, joint inflammation, or neurological impairment.': 'मांसपेशियों की कमजोरी, जोड़ों की सूजन या तंत्रिका संबंधी कमजोरी के कारण बकरी को खड़े होने या चलने में कठिनाई हो रही है।',
        'The goat has stopped eating, which is a primary indicator of pain, fever, metabolic disturbance, or stress.': 'बकरी ने खाना बंद कर दिया है, जो दर्द, बुखार, चयापचय में गड़बड़ी या तनाव का मुख्य संकेतक है।',
        'The goat is foaming at the mouth, which suggests acute poisoning, a severe neurological condition, or a physical blockage in the throat.': 'बकरी के मुंह से झाग निकल रहा है, जो तीव्र विषाक्तता, गंभीर तंत्रिका संबंधी स्थिति या गले में शारीरिक रुकावट का संकेत देता है।',
        'The goat is losing muscle mass over time due to chronic nutrient malabsorption, poor diet, or a long-term wasting infection.': 'बकरी पुरानी पोषक तत्व कुअवशोषण, खराब आहार या दीर्घकालिक बीमारी के कारण मांसपेशियों को खो रही है।',
        'The goat exhibits stiff and rigid muscles, which is a classic sign of tetanus infection, typically entering through an untreated wound or castration site.': 'बकरी कठोर और जकड़ी हुई मांसपेशियों को प्रदर्शित करती है, जो टिटनेस संक्रमण का एक क्लासिक संकेत है, आमतौर पर बिना इलाज वाले घाव या बधियाकरण स्थान से प्रवेश करता है।',
        'The goat has nasal discharge due to irritation or infection in its upper or lower respiratory tract.': 'ऊपरी या निचले श्वसन मार्ग में जलन या संक्रमण के कारण बकरी की नाक से स्राव हो रहा है।',
        'The goat has neck rigidity or abnormal posture, indicating a neurological disturbance, commonly thiamine deficiency or bacterial infection of the brain.': 'बकरी की गर्दन में अकड़न या असामान्य मुद्रा है, जो तंत्रिका संबंधी गड़बड़ी का संकेत देती है, आमतौर पर थायमिन की कमी या मस्तिष्क के जीवाणु संक्रमण के कारण।',
        'The goat exhibits shaking and twitching due to nervous system overstimulation, which can be caused by toxins, mineral lack, or brain inflammation.': 'बकरी तंत्रिका तंत्र के अति-उत्तेजना के कारण कांप रही है और फड़क रही है, जो विषाक्त पदार्थों, खनिजों की कमी या मस्तिष्क की सूजन के कारण हो सकता है।',
        'The goat has poor vision in dim light, which is a classic symptom of vitamin A deficiency due to lack of green fodder.': 'बकरी को कम रोशनी में धुंधला दिखाई देता है, जो हरे चारे की कमी के कारण विटामिन ए की कमी का एक क्लासिक लक्षण है।',
        'Avoid feeding extremely coarse or thorny forage': 'अत्यधिक मोटे या कांटेदार चारे को खिलाने से बचें',
        'Regularly inspect teeth and mouth for injuries': 'चोटों के लिए दांतों और मुंह का नियमित रूप से निरीक्षण करें',
        'Maintain clean feeding troughs': 'चारा खिलाने वाले गर्त को साफ रखें',
        'Provide a balanced diet and avoid sudden feed changes': 'संतुलित आहार प्रदान करें और अचानक चारा बदलने से बचें',
        'Implement a regular deworming schedule': 'नियमित कृमिनाशक कार्यक्रम लागू करें',
        'Ensure constant access to clean water': 'साफ पानी तक लगातार पहुंच सुनिश्चित करें',
        'Provide a clean, well-ventilated housing': 'साफ, अच्छी तरह हवादार आवास प्रदान करें',
        'Ensure adequate nutrition and mineral supplements': 'पर्याप्त पोषण और खनिज पूरक सुनिश्चित करें',
        'Keep water clean and accessible': 'पानी को साफ और सुलभ रखें',
        'Ensure balanced mineral intake, especially for pregnant/lactating goats': 'संतुलित खनिज सेवन सुनिश्चित करें, विशेष रूप से गर्भवती/दूध पिलाने वाली बकरियों के लिए',
        'Maintain dry and clean bedding to prevent joint infections': 'जोड़ों के संक्रमण को रोकने के लिए सूखा और साफ बिछौना बनाए रखें',
        'Keep paths clear of hazards': 'रास्तों को खतरों से मुक्त रखें',
        'Introduce new feed gradually': 'नया चारा धीरे-धीरे शुरू करें',
        'Avoid moldy or spoiled feed': 'फफूंदयुक्त या खराब चारे से बचें',
        'Minimize stress in the herd': 'झुंड में तनाव कम करें',
        'Keep pesticides and chemical products locked away': 'कीटनाशकों और रासायनिक उत्पादों को ताले में रखें',
        'Prevent access to toxic weeds or pasture areas': 'जहरीली खरपतवार या चरागाह क्षेत्रों तक पहुंच को रोकें',
        'Vaccinate against rabies where applicable': 'जहां लागू हो, रेबीज के खिलाफ टीकाकरण करें',
        'Run regular fecal tests and deworm accordingly': 'नियमित गोबर परीक्षण चलाएं और उसी के अनुसार कृमिनाशक दें',
        'Provide feed with adequate protein and energy content': 'पर्याप्त प्रोटीन और ऊर्जा सामग्री वाला चारा प्रदान करें',
        'Quarantine new stock to prevent wasting diseases': 'बीमारियों को फैलने से रोकने के लिए नए पशुओं को क्वारंटाइन करें',
        'Vaccinate goats with Tetanus Toxoid': 'बकरियों को टिटनेस टॉक्साइड का टीका लगाएं',
        'Disinfect all wounds and use sterile tools for castration/docking': 'सभी घावों को कीटाणुरहित करें और बधियाकरण के लिए निष्फल उपकरणों का उपयोग करें',
        'Ensure clean kidding environments': 'बच्चे देने के लिए स्वच्छ वातावरण सुनिश्चित करें',
        'Avoid overcrowded, dusty, or drafty housing': 'अत्यधिक भीड़भाड़ वाले, धूल भरे या ठंडी हवा वाले आवास से बचें',
        'Vaccinate against pasteurellosis': 'पाश्चरेलोसिस के खिलाफ टीकाकरण करें',
        'Provide adequate ventilation in the shed': 'बाड़े में पर्याप्त वेंटिलेशन प्रदान करें',
        'Avoid feeding moldy silage or sudden carbohydrate excess': 'फफूंदयुक्त साइलेज या अचानक कार्बोहाइड्रेट की अधिकता खिलाने से बचें',
        'Maintain clean feed and water supply': 'साफ चारे और पानी की आपूर्ति बनाए रखें',
        'Provide mineral supplements containing thiamine': 'थायमिन युक्त खनिज पूरक प्रदान करें',
        'Inspect pastures for toxic weeds and discard moldy feed': 'जहरीली खरपतवारों के लिए चरागाहों का निरीक्षण करें और फफूंदयुक्त चारे को फेंक दें',
        'Provide complete mineral block containing magnesium and calcium': 'मैग्नीशियम और कैल्शियम युक्त पूर्ण खनिज ब्लॉक प्रदान करें',
        'Ensure shelter from extreme cold': 'अत्यधिक ठंड से सुरक्षा सुनिश्चित करें',
        'Provide adequate green fodder or silage': 'पर्याप्त हरा चारा या साइलेज प्रदान करें',
        'Feed vitamin A supplements regularly during dry seasons': 'सूखे मौसम में नियमित रूप से विटामिन ए सप्लीमेंट दें',
        'Ensure adequate nutrition for pregnant does': 'गर्भवती बकरियों के लिए पर्याप्त पोषण सुनिश्चित करें',
        'Antibiotics (Penicillin/Streptomycin under vet advice)': 'एंटीबायोटिक्स (पशु चिकित्सक की सलाह पर पेनिसिलिन/स्ट्रेप्टोमाइसिन)',
        'Anti-inflammatory drugs': 'एंटी-इंफ्लेमेटरी दवाएं',
        'Antispasmodics': 'ऐंठनरोधी दवाएं',
        'Dewormers (if caused by parasites)': 'कृमिनाशक (यदि परजीवी के कारण हो)',
        'Carminative mixtures for gas relief': 'गैस राहत के लिए कार्मिनिटिव मिश्रण',
        'Multivitamin supplements': 'मल्टीविटामिन सप्लीमेंट',
        'Supportive electrolytes': 'सहायक इलेक्ट्रोलाइट्स',
        'Antipyretics if fever is present': 'बुखार होने पर एंटीपीयरेटिक्स',
        'Calcium borogluconate (if metabolic)': 'कैल्शियम बो्रोग्लूकोनेट (यदि चयापचय संबंधी हो)',
        'Vitamin B-complex (especially Thiamine)': 'विटामिन बी-कॉम्प्लेक्स (विशेष रूप से थायमिन)',
        'Anti-inflammatories': 'विरोधी भड़काऊ दवाएं',
        'Rumen tonic/appetizers': 'रुमेन टॉनिक/भूख बढ़ाने वाली दवाएं',
        'Dewormers (if chronic)': 'कृमिनाशक (यदि पुराना हो)',
        'Atropine sulfate (antidote for organophosphate poisoning)': 'एट्रोपिन सल्फेट (ऑर्गेनोफॉस्फेट विषाक्तता का मारक)',
        'Activated charcoal': 'सक्रिय चारकोल',
        'Anticonvulsants': 'आक्षेपरोधी दवाएं',
        'Broad-spectrum dewormers': 'व्यापक-स्पेक्ट्रम कृमिनाशक',
        'Protein concentrates': 'प्रोटीन सांद्रता',
        'Mineral supplements': 'खनिज पूरक',
        'Tetanus antitoxin': 'टिटनेस एंटीटॉक्सिन',
        'Penicillin/Antibiotics': 'पेनिसिलिन/एंटीबायोटिक्स',
        'Muscle relaxants/Sedatives': 'मांसपेशियों को आराम देने वाली दवाएं/शामक',
        'Broad-spectrum antibiotics': 'ब्रॉड-स्पेक्ट्रम एंटीबायोटिक्स',
        'Mucolytics/Expectorants': 'म्यूकोलिटिक्स/कफोत्सारक',
        'Dewormers for nasal bots': 'नाक के बोट के लिए कृमिनाशक',
        'Thiamine (Vitamin B1) injections': 'थायमिन (विटामिन बी 1) इंजेक्शन',
        'High-dose antibiotics (e.g., penicillin for listeriosis)': 'उच्च खुराक वाले एंटीबायोटिक्स (जैसे, लिस्टेरियोसिस के लिए पेनिसिलिन)',
        'Corticosteroids': 'कोर्टिकोस्टेरॉइड्स',
        'Magnesium sulfate / Calcium injections': 'मैग्नीशियम सल्फेट / कैल्शियम इंजेक्शन',
        'Activated charcoal (if poisoning is suspected)': 'सक्रिय चारकोल (यदि विषाक्तता का संदेह हो',
        'Vitamin B-complex': 'विटामिन बी-कॉम्प्लेक्स',
        'Vitamin A injections or oral supplements': 'विटामिन ए इंजेक्शन या मौखिक सप्लीमेंट',
        'Antibiotic eye ointments (if pink eye is present)': 'एंटीबायोटिक आई ऑइंटमेंट (यदि आंख आ रही हो)',
        'Isolate the goat to ensure easy access to feed': 'चारा खाने तक आसान पहुंच सुनिश्चित करने के लिए बकरी को अलग करें',
        'Provide soft, non-abrasive, easily chewable feed': 'नरम, गैर-खुरदरा, आसानी से चबाने योग्य चारा प्रदान करें',
        'Consult a veterinarian immediately': 'तुरंत एक पशु चिकित्सक से परामर्श करें',
        'Isolate the animal in a comfortable space': 'पशु को एक आरामदायक स्थान पर अलग करें',
        'Do not force-feed the goat': 'बकरी को जबरदस्ती खाना न खिलाएं',
        'Call a veterinarian immediately as colic can be fatal': 'तुरंत पशु चिकित्सक को बुलाएं क्योंकि पेट का दर्द घातक हो सकता है',
        'Move the goat to a cool, shaded, well-ventilated area': 'बकरी को ठंडे, छायादार, अच्छी हवादार जगह पर ले जाएं',
        'Offer clean fresh water and electrolytes': 'साफ ताजा पानी और इलेक्ट्रोलाइट्स प्रदान करें',
        'Contact a veterinarian to diagnose the root cause': 'मूल कारण का निदान करने के लिए पशु चिकित्सक से संपर्क करें',
        'Place the goat on thick, dry bedding to prevent sores': 'घावों को रोकने के लिए बकरी को मोटे, सूखे बिछौने पर रखें',
        'Provide food and water within easy reach': 'आसानी से पहुंचने योग्य भोजन और पानी प्रदान करें',
        'Consult a vet for neurological or metabolic assessment': 'न्यूरोलॉजिकल या चयापचय मूल्यांकन के लिए पशु चिकित्सक से परामर्श करें',
        'Isolate the goat to monitor its feed intake': 'चारा खाने की निगरानी के लिए बकरी को अलग करें',
        'Offer fresh, highly palatable browse (leaves) or grass': 'ताजा, अत्यधिक स्वादिष्ट पत्ते या घास प्रदान करें',
        'Check body temperature for fever': 'बुखार के लिए शरीर के तापमान की जांच करें',
        'Handle the goat carefully using protective gloves': 'सुरक्षात्मक दस्ताने का उपयोग करके बकरी को सावधानी से संभालें',
        'Check for visible blockages in the mouth without getting bitten': 'बिना काटे मुंह में दिखाई देने वाली रुकावटों की जांच करें',
        'Provide the affected goat with high-quality, high-protein feed separately': 'प्रभावित बकरी को अलग से उच्च गुणवत्ता वाला, उच्च प्रोटीन चारा प्रदान करें',
        'Ensure the goat is not bullied by others during feeding': 'यह सुनिश्चित करें कि चारे के समय अन्य पशु बकरी को परेशान न करें',
        'Get a veterinary evaluation for chronic diseases': 'पुरानी बीमारियों के लिए पशु चिकित्सा मूल्यांकन प्राप्त करें',
        'Place the goat in a quiet, dark, and deeply bedded stall to avoid spasms': 'ऐंठन से बचने के लिए बकरी को एक शांत, अंधेरे और गहरे बिस्तरों वाले बाड़े में रखें',
        'Keep food and water at chest level': 'भोजन और पानी को छाती के स्तर पर रखें',
        'Call a vet urgently': 'तुरंत पशु चिकित्सक को बुलाएं',
        'Isolate the goat to prevent spreading respiratory droplets': 'श्वसन बूंदों को फैलने से रोकने के लिए बकरी को अलग करें',
        'Keep the animal warm, dry, and sheltered': 'पशु को गर्म, सूखा और आश्रय में रखें',
        'Clean the nostrils with a soft damp cloth': 'मुलायम नम कपड़े से नथुने साफ करें',
        'Isolate in a safe, padded stall to prevent injury from circling/falling': 'चक्कर आने/गिरने से चोट को रोकने के लिए एक सुरक्षित, गद्देदार बाड़े में अलग करें',
        'Support the head if the goat is unable to lift it': 'यदि बकरी सिर उठाने में असमर्थ है तो सिर को सहारा दें',
        'Seek urgent vet care': 'तुरंत पशु चिकित्सा देखभाल लें',
        'Move the goat to a warm, quiet, stress-free shelter': 'बकरी को गर्म, शांत, तनाव मुक्त आश्रय में ले जाएं',
        'Prevent self-injury by removing sharp objects': 'नुकीली चीजों को हटाकर खुद को चोट पहुंचाने से रोकें',
        'Call a veterinarian immediately': 'तुरंत एक पशु चिकित्सक को बुलाएं',
        'Keep the blind goat in a safe, familiar pen before sunset': 'सूर्यास्त से पहले अंधी बकरी को एक सुरक्षित, परिचित बाड़े में रखें',
        'Provide easily accessible feed and water': 'आसानी से उपलब्ध भोजन और पानी प्रदान करें',
        'Consult a vet for nutritional support': 'पोषण संबंधी सहायता के लिए पशु चिकित्सक से परामर्श करें',
        'Soft green leaves, browse, and wet mash or gruel': 'नरम हरी पत्तियां, चारा, और गीला दलिया',
        'Ensure clean drinking water with electrolyte support': 'इलेक्ट्रोलाइट सहायता के साथ साफ पीने का पानी सुनिश्चित करें',
        'Fresh green leaves, high-quality hay': 'ताजा हरी पत्तियां, उच्च गुणवत्ता वाली सूखी घास',
        'Provide fresh, clean water': 'ताजा, साफ पानी प्रदान करें',
        'High-energy digestible feed, green browse': 'उच्च ऊर्जा वाला सुपाच्य चारा, हरी पत्तियां',
        'Clean water with electrolytes': 'इलेक्ट्रोलाइट्स के साथ साफ पानी',
        'Legume hay, fresh browse': 'फलीदार घास, ताजा पत्तियां',
        'Keep fresh water close to the animal': 'पशु के पास साफ पानी रखें',
        'Palatable leaves (like mulberry or jackfruit leaves)': 'स्वादिष्ट पत्तियां (जैसे शहतूत या कटहल के पत्ते)',
        'Ensure clean drinking water': 'साफ पीने का पानी सुनिश्चित करें',
        'Withhold food initially until veterinarian examines': 'पशु चिकित्सक के परीक्षण तक शुरू में भोजन रोकें',
        'Provide clean water if goat is stable and able to swallow': 'यदि बकरी स्थिर है और निगलने में सक्षम है तो साफ पानी प्रदान करें',
        'Leguminous fodder, concentrate feed': 'फलीदार चारा, संतुलित पशु आहार',
        'Mineral block supplementation': 'खनिज ब्लॉक अनुपूरण',
        'Easy-to-swallow soft feed or gruel': 'निगलने में आसान नरम चारा या दलिया',
        'Keep fresh water close to chest level': 'ताजा पानी छाती के स्तर के पास रखें',
        'Dust-free high-quality green browse': 'धूल मुक्त उच्च गुणवत्ता वाली हरी पत्तियां',
        'Offer fresh palatable feed and support while feeding if needed': 'यदि आवश्यक हो तो ताजा स्वादिष्ट चारा दें और चारे के दौरान सहायता करें',
        'Provide water close to head level': 'सिर के स्तर के पास पानी प्रदान करें',
        'Provide clean, fresh water and soft green grass': 'साफ, ताजा पानी और नरम हरी घास प्रदान करें',
        'Mineral mixtures containing magnesium': 'मैग्नीशियम युक्त खनिज मिश्रण',
        'Fresh green leaves, carrots, high-quality grass hay': 'ताजी हरी पत्तियां, गाजर, उच्च गुणवत्ता वाली सूखी घास',
        'Mineral and vitamin mix': 'खनिज और विटामिन मिश्रण',
        'Clean feeding troughs to prevent bacterial buildup': 'बैक्टीरिया के निर्माण को रोकने के लिए चारा खिलाने वाले गर्त को साफ करें',
        'Sanitize any equipment used to inspect the mouth': 'मुंह का निरीक्षण करने के लिए उपयोग किए जाने वाले किसी भी उपकरण को साफ करें',
        'Keep the goat shelter clean and dry': 'बकरी के आश्रय को साफ और सूखा रखें',
        'Sanitize feeding troughs regularly': 'चारा गर्त को नियमित रूप से साफ करें',
        'Maintain dry bedding to prevent secondary infections': 'माध्यमिक संक्रमण को रोकने के लिए सूखा बिछौना बनाए रखें',
        'Provide adequate ventilation in the housing': 'आवास में पर्याप्त वेंटिलेशन प्रदान करें',
        'Ensure soft and dry flooring to prevent foot rot or joint injuries': 'खुर सड़न या जोड़ों की चोटों को रोकने के लिए नरम और सूखी फर्श सुनिश्चित करें',
        'Clean the pen floor regularly': 'बाड़े के फर्श को नियमित रूप से साफ करें',
        'Remove uneaten wet feed to prevent mold growth': 'फफूंद के विकास को रोकने के लिए न खाया हुआ गीला चारा हटा दें',
        'Maintain overall cleanliness of feeding zones': 'चारा खिलाने वाले क्षेत्रों की समग्र सफाई बनाए रखें',
        'Wear gloves when handling foaming goats (zoonotic rabies risk)': 'झाग वाली बकरियों को संभालते समय दस्ताने पहनें (रेबीज का खतरा)',
        'Disinfect the area and isolate the goat immediately': 'क्षेत्र को कीटाणुरहित करें और बकरी को तुरंत अलग करें',
        'Maintain pasture rotation to prevent worm reinfection': 'कीड़ों के पुन: संक्रमण को रोकने के लिए चरागाह रोटेशन बनाए रखें',
        'Disinfect the quarantine area regularly': 'संगरोध (क्वारंटाइन) क्षेत्र को नियमित रूप से कीटाणुरहित करें',
        'Perform surgeries in dry, clean, and sterilized areas': 'सूखे, साफ और निष्फल क्षेत्रों में सर्जरी करें',
        'Ensure deep, clean straw bedding': 'गहरे, साफ पुआल के बिछौने सुनिश्चित करें',
        'Ventilate the shed properly to reduce ammonia buildup': 'अमोनिया के निर्माण को कम करने के लिए बाड़े को ठीक से हवादार करें',
        'Clean the housing area daily': 'आवास क्षेत्र को प्रतिदिन साफ करें',
        'Avoid feeding spoiled or poorly fermented silage': 'खराब या खराब रूप से किण्वित साइलेज खिलाने से बचें',
        'Ensure clean and sanitized troughs': 'साफ और स्वच्छ गर्त सुनिश्चित करें',
        'Keep bedding clean, soft, and dry': 'बिछौना साफ, मुलायम और सूखा रखें',
        'Isolate in a peaceful, noise-free area': 'एक शांत, शोर-मुक्त क्षेत्र में अलग करें',
        "Remove obstacles from the blind goat's living space": 'अंधी बकरी के रहने के स्थान से बाधाओं को हटा दें',
        'Maintain clean housing to prevent eye flies or irritants': 'कण्ठ मक्खियों या जलन पैदा करने वाले तत्वों को रोकने के लिए साफ आवास बनाए रखें',
    }
}

# Load expanded translations if available
try:
    import json
    import os
    _expanded_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "translations_expanded.json")
    if os.path.exists(_expanded_path):
        with open(_expanded_path, "r", encoding="utf-8") as f:
            _expanded_data = json.load(f)
            for lang in ["hi", "kn"]:
                if lang in _expanded_data:
                    if lang not in TRANSLATIONS:
                        TRANSLATIONS[lang] = {}
                    TRANSLATIONS[lang].update(_expanded_data[lang])
        print(f"[INFO] Loaded expanded translations from {_expanded_path}")
except Exception as e:
    print(f"[WARN] Failed to load expanded translations: {e}")


def get_validation_message(message_key: str, lang: str, **kwargs) -> str:
    """Gets and formats a validation message in the specified language."""
    # Ensure lang is one of 'en', 'hi', 'kn'
    lang_code = lang.lower()
    if lang_code not in ["en", "hi", "kn"]:
        lang_code = "en"
        
    validation_map = TRANSLATIONS.get("validation", {})
    message_dict = validation_map.get(message_key, {})
    message_template = message_dict.get(lang_code, message_dict.get("en", "Validation error"))
    
    # Translate the animal names in kwargs if they exist
    translated_kwargs = {}
    for k, v in kwargs.items():
        if isinstance(v, str):
            # Try to translate animal name (Cow -> गाय, etc)
            animal_name = v.lower()
            # We map the lowercase animal name back to title case for lookup if needed,
            # or just look it up directly.
            # E.g. 'cow' -> 'Cow' in english, 'गाय' in Hindi
            capitalized = animal_name.capitalize()
            # If we have a translation for the capitalized animal name (like "Cow")
            # in our main dict, use it. But wait, "Cow" is not in the dict directly for kn/hi?
            # Actually, looking at TRANSLATIONS, they might not have standalone animal names.
            # Let's check TRANSLATIONS for 'Cow'. It is not there. We should add it or just return v.
            # Wait, I will just format the template. The frontend translates animal names anyway, but for backend errors...
            # The user requested Cow -> गाय / ಹಸು. I'll add a helper inside for common animals.
            animal_translations = {
                "en": {"cow": "cow", "goat": "goat", "sheep": "sheep", "human": "human", "dog": "dog", "cat": "cat", "bird": "bird", "horse": "horse", "monkey": "monkey", "wild animal": "wild animal", "random object": "random object", "unknown": "unknown"},
                "hi": {"cow": "गाय", "goat": "बकरी", "sheep": "भेड़", "human": "इंसान", "dog": "कुत्ता", "cat": "बिल्ली", "bird": "पक्षी", "horse": "घोड़ा", "monkey": "बंदर", "wild animal": "जंगली जानवर", "random object": "अमान्य वस्तु", "unknown": "अज्ञात"},
                "kn": {"cow": "ಹಸು", "goat": "ಆಡು", "sheep": "ಕುರಿ", "human": "ಮಾನವ", "dog": "ನಾಯಿ", "cat": "ಬೆಕ್ಕು", "bird": "ಪಕ್ಷಿ", "horse": "ಕುದುರೆ", "monkey": "ಕೋತಿ", "wild animal": "ಕಾಡು ಪ್ರಾಣಿ", "random object": "ಯಾದೃಚ್ಛಿಕ ವಸ್ತು", "unknown": "ಅಜ್ಞಾತ"}
            }
            if animal_name in animal_translations.get(lang_code, {}):
                trans_val = animal_translations[lang_code][animal_name]
                if k == 'detected' and lang_code == 'en':
                    trans_val = trans_val.capitalize()
                translated_kwargs[k] = trans_val
            else:
                translated_kwargs[k] = v.capitalize() if (k == 'detected' and lang_code == 'en') else v
        else:
            translated_kwargs[k] = v
            
    return message_template.format(**translated_kwargs)

def translate_free_sync(text: str, target_lang: str) -> str:
    """Synchronous fallback translation using Google's free translation web service."""
    if not text or not target_lang or target_lang.lower() == "en":
        return text
    import urllib.parse
    import urllib.request
    import json
    try:
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_lang}&dt=t&q={urllib.parse.quote(text)}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=1.5) as response:
            data = json.loads(response.read().decode('utf-8'))
            res = "".join([part[0] for part in data[0] if part[0]])
            if res:
                return res
    except Exception:
        pass
    return text

def translate_str(text: str, lang: str) -> str:
    """Translates a single string using lookup tables with dynamic fallback."""
    if not lang or lang == "en":
        return text
    
    lang_map = TRANSLATIONS.get(lang.lower())
    if not lang_map:
        return text
        
    if text in lang_map:
        return lang_map[text]
        
    # Dynamic fallback if not found in dictionary
    translated = translate_free_sync(text, lang)
    if translated != text:
        lang_map[text] = translated
    return translated

def translate_list(items: list, lang: str) -> list:
    """Translates a list of strings."""
    if not lang or lang == "en":
        return items
        
    lang_map = TRANSLATIONS.get(lang.lower())
    if not lang_map:
        return items
        
    res = []
    for item in items:
        if item in lang_map:
            res.append(lang_map[item])
        else:
            translated = translate_free_sync(item, lang)
            if translated != item:
                lang_map[item] = translated
            res.append(translated)
    return res

def translate_disease_data(disease_dict: dict, lang: str) -> dict:
    """
    Translates disease details dictionary.
    Returns a copy of the dictionary with translated values.
    """
    if not lang or lang == "en":
        # Add empty emergency field if not present for schema compatibility
        result = dict(disease_dict)
        if "severity" in disease_dict and disease_dict["severity"] in ["Critical", "High"]:
            result["emergency"] = "Emergency Veterinary Attention Required: This disease is severe. Immediately isolate the animal and contact a veterinary doctor."
        else:
            result["emergency"] = ""
        return result
        
    result = dict(disease_dict)
    
    # Translate single string fields
    if "name" in result:
        result["name"] = translate_str(result["name"], lang)
    if "disease_name" in result:
        result["disease_name"] = translate_str(result["disease_name"], lang)
    if "severity" in result:
        severity_lower = result["severity"].lower()
        translated_severity = TRANSLATIONS.get(lang.lower(), {}).get(severity_lower, result["severity"])
        result["severity"] = translated_severity
    if "why_it_happened" in result:
        result["why_it_happened"] = translate_str(result["why_it_happened"], lang)
        
    # Translate list fields
    if "symptoms" in result:
        result["symptoms"] = translate_list(result["symptoms"], lang)
    if "causes" in result:
        result["causes"] = translate_list(result["causes"], lang)
    if "prevention" in result:
        result["prevention"] = translate_list(result["prevention"], lang)
    if "medicine" in result:
        result["medicine"] = translate_list(result["medicine"], lang)
    if "first_aid" in result:
        result["first_aid"] = translate_list(result["first_aid"], lang)
    if "food_recommendations" in result:
        result["food_recommendations"] = translate_list(result["food_recommendations"], lang)
    if "hygiene_tips" in result:
        result["hygiene_tips"] = translate_list(result["hygiene_tips"], lang)
        
    # Translate emergency text
    if "severity" in disease_dict and disease_dict["severity"] in ["Critical", "High"]:
        result["emergency"] = TRANSLATIONS.get(lang.lower(), {}).get("emergency_alert", "Emergency Veterinary Attention Required: This disease is severe. Immediately isolate the animal and contact a veterinary doctor.")
    else:
        result["emergency"] = ""
        
    return result


async def translate_text(text: str, target_lang: str) -> str:
    """
    Translates a block of text dynamically using the Gemini API or a free fallback service.
    Handles 'en', 'hi', and 'kn'.
    """
    if not text or not target_lang or target_lang.lower() == "en":
        return text

    import httpx
    from ..config import settings
    
    # Clean language code
    target_lang = target_lang.lower().strip()
    if target_lang == "en":
        return text

    # Map target language code to human-readable name for Gemini
    lang_names = {
        "hi": "Hindi",
        "kn": "Kannada",
        "en": "English"
    }
    
    target_name = lang_names.get(target_lang, "English")
    
    # Try Gemini translation if key is configured
    if settings.GEMINI_API_KEY:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={settings.GEMINI_API_KEY}"
        
        if target_lang == "en":
            prompt = (
                "Translate the following text to English. "
                "Preserve all markdown formatting (like **, *, -, \n, bullet points), emojis, and livestock/veterinary terms. "
                "Do not translate standard medicine names. "
                "Only return the exact translated text without any explanation or extra text.\n\n"
                f"Text to translate:\n{text}"
            )
        else:
            prompt = (
                f"Translate the following English text to {target_name}. "
                "Preserve all markdown formatting (like **, *, -, \n, bullet points), emojis, and livestock/veterinary terms. "
                "Keep veterinary medicine names and proper names in standard script or transliterated as standard. "
                "Only return the exact translated text without any explanation or extra text.\n\n"
                f"Text to translate:\n{text}"
            )

        payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ],
            "generationConfig": {
                "temperature": 0.1,
                "maxOutputTokens": 2048
            }
        }
        
        try:
            async with httpx.AsyncClient(timeout=15.0) as client:
                response = await client.post(url, json=payload)
                if response.status_code == 200:
                    res_json = response.json()
                    candidates = res_json.get("candidates", [])
                    if candidates:
                        parts = candidates[0].get("content", {}).get("parts", [])
                        if parts:
                            translated = parts[0].get("text", "").strip()
                            if translated:
                                return translated
                print(f"[WARN] Gemini Translation API returned status code {response.status_code}: {response.text}")
        except Exception as e:
            print(f"[ERROR] Dynamic translation via Gemini failed: {e}")

    # Fallback to free Google Translate API if Gemini is not configured or failed
    try:
        import urllib.parse
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl={target_lang}&dt=t&q={urllib.parse.quote(text)}"
        async with httpx.AsyncClient(timeout=8.0) as client:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = await client.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                res = "".join([part[0] for part in data[0] if part[0]])
                if res:
                    return res
    except Exception as e:
        print(f"[WARN] Free Google Translate fallback failed in translate_text: {e}")
        
    return text

