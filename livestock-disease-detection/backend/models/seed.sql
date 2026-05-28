INSERT INTO diseases (name, animal_type, description, treatment) VALUES
(
  'Foot and Mouth Disease (FMD)',
  'cow',
  'A highly contagious viral disease affecting cloven-hoofed animals. It causes fever and blister-like sores on the tongue and lips, in the mouth, on the teats, and between the hooves.',
  'There is no specific treatment for FMD. Supportive care includes cleaning lesions with mild disinfectants, providing soft feed, and keeping the animals dry. Vaccination is the key prevention method.'
),
(
  'Mastitis',
  'cow',
  'Inflammation of the mammary gland (udder) usually caused by bacterial infection. Symptoms include swelling, pain, heat, redness, and abnormal milk (clots, wateriness, or blood).',
  'Treatment involves intramammary infusions of antibiotics, anti-inflammatory drugs to reduce pain and swelling, and frequent stripping of the affected quarters.'
),
(
  'Anthrax',
  'sheep',
  'A serious infectious disease caused by Bacillus anthracis. Symptoms include sudden death, high fever, and dark blood oozing from natural body openings.',
  'Immediate treatment with high doses of penicillin or tetracycline is required if caught early. Vaccination is critical, and carcasses should be burned or buried deep with quicklime.'
),
(
  'Peste des Petits Ruminants (PPR)',
  'goat',
  'A highly contagious viral disease affecting goats and sheep. It causes high fever, nasal discharge, sores in the mouth, breathing difficulties, and severe diarrhea.',
  'Supportive therapy with antibiotics for secondary bacterial infections, rehydration, and lesion care. Annual vaccination is highly effective for control.'
)
ON CONFLICT DO NOTHING;
