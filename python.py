import json

# Accurate data for generating the JSON file
data = {
    "diseases": [
        {
            "name": "Migraine",
            "symptoms": ["headache", "nausea", "sensitivity to light", "sensitivity to sound"],
            "doctors": ["Neurologist"]
        },
        {
            "name": "COVID-19",
            "symptoms": ["fever", "cough", "shortness of breath", "fatigue", "loss of taste", "loss of smell"],
            "doctors": ["General Physician", "Infectious Disease Specialist"]
        },
        {
            "name": "Heart Attack",
            "symptoms": ["chest pain", "shortness of breath", "nausea", "sweating"],
            "doctors": ["Cardiologist"]
        },
        {
            "name": "Common Cold",
            "symptoms": ["sneezing", "cold", "runny nose", "sore throat", "cough"],
            "doctors": ["General Physician"]
        },
        {
            "name": "Flu",
            "symptoms": ["fever", "cold", "chills", "muscle aches", "cough", "fatigue"],
            "doctors": ["General Physician"]
        },
        {
            "name": "Asthma",
            "symptoms": ["wheezing", "shortness of breath", "chest tightness", "cough"],
            "doctors": ["Pulmonologist"]
        },
        {
            "name": "Diabetes",
            "symptoms": ["frequent urination", "excessive thirst", "extreme hunger", "unexplained weight loss", "fatigue"],
            "doctors": ["Endocrinologist"]
        },
        {
            "name": "Hypertension",
            "symptoms": ["headache", "shortness of breath", "nosebleeds", "chest pain"],
            "doctors": ["Cardiologist"]
        },
        {
            "name": "Bronchitis",
            "symptoms": ["cough", "mucus production", "fatigue", "shortness of breath", "fever"],
            "doctors": ["Pulmonologist"]
        },
        {
            "name": "Pneumonia",
            "symptoms": ["cough", "fever", "chills", "shortness of breath"],
            "doctors": ["Pulmonologist"]
        },
        {
            "name": "Depression",
            "symptoms": ["laziness", "headache", "anxiety", "procrastination"],
            "doctors": ["Therapist"]
        },
        {
            "name": "Anxiety Disorder",
            "symptoms": ["nervousness", "restlessness", "fatigue", "difficulty concentrating"],
            "doctors": ["Psychiatrist"]
        },
        {
            "name": "Chickenpox",
            "symptoms": ["itchy rash", "blisters", "fever", "tiredness"],
            "doctors": ["Pediatrician", "General Physician"]
        },
        {
            "name": "Hepatitis A",
            "symptoms": ["fatigue", "nausea", "abdominal pain", "loss of appetite", "fever"],
            "doctors": ["Gastroenterologist"]
        },
        {
            "name": "Gastritis",
            "symptoms": ["nausea", "vomiting", "stomach pain", "loss of appetite"],
            "doctors": ["Gastroenterologist"]
        },
        {
            "name": "Eczema",
            "symptoms": ["itchy skin", "red rash", "dry skin", "swelling"],
            "doctors": ["Dermatologist"]
        },
        {
            "name": "Psoriasis",
            "symptoms": ["red patches", "scaly skin", "itching", "pain"],
            "doctors": ["Dermatologist"]
        },
        {
            "name": "Osteoporosis",
            "symptoms": ["back pain", "loss of height", "stooped posture", "bone fractures"],
            "doctors": ["Orthopedist"]
        },
        {
            "name": "Rheumatoid Arthritis",
            "symptoms": ["joint pain", "swelling", "stiffness", "fatigue"],
            "doctors": ["Rheumatologist"]
        },
        {
            "name": "Gout",
            "symptoms": ["severe joint pain", "redness", "swelling", "heat"],
            "doctors": ["Rheumatologist"]
        },
        {
            "name": "Sinusitis",
            "symptoms": ["nasal congestion", "headache", "facial pain", "runny nose"],
            "doctors": ["ENT Specialist"]
        },
        {
            "name": "Appendicitis",
            "symptoms": ["abdominal pain", "loss of appetite", "nausea", "vomiting", "fever"],
            "doctors": ["Surgeon"]
        },
        {
            "name": "UTI",
            "symptoms": ["frequent urination", "burning sensation", "cloudy urine", "pelvic pain"],
            "doctors": ["Urologist"]
        },
        {
            "name": "Acne",
            "symptoms": ["pimples", "blackheads", "whiteheads", "oily skin"],
            "doctors": ["Dermatologist"]
        },
        {
            "name": "Hypothyroidism",
            "symptoms": ["fatigue", "weight gain", "cold intolerance", "dry skin"],
            "doctors": ["Endocrinologist"]
        },
        {
            "name": "Hyperthyroidism",
            "symptoms": ["weight loss", "rapid heartbeat", "nervousness", "sweating"],
            "doctors": ["Endocrinologist"]
        },
        {
            "name": "Tuberculosis",
            "symptoms": ["persistent cough", "weight loss", "night sweats", "fever"],
            "doctors": ["Infectious Disease Specialist"]
        },
        {
            "name": "HIV/AIDS",
            "symptoms": ["fever", "chills", "rash", "night sweats", "fatigue"],
            "doctors": ["Infectious Disease Specialist"]
        },
        {
            "name": "Chlamydia",
            "symptoms": ["painful urination", "lower abdominal pain", "discharge", "pain during intercourse"],
            "doctors": ["Gynecologist", "Urologist"]
        },
        {
            "name": "Gonorrhea",
            "symptoms": ["painful urination", "pus-like discharge", "testicular pain", "pelvic pain"],
            "doctors": ["Gynecologist", "Urologist"]
        },
        {
            "name": "Syphilis",
            "symptoms": ["painless sore", "rash", "fever", "swollen lymph nodes"],
            "doctors": ["Infectious Disease Specialist"]
        },
        {
            "name": "Multiple Sclerosis",
            "symptoms": ["numbness", "tingling", "muscle weakness", "vision problems"],
            "doctors": ["Neurologist"]
        },
        {
            "name": "Parkinson's Disease",
            "symptoms": ["tremor", "slowed movement", "rigid muscles", "impaired posture"],
            "doctors": ["Neurologist"]
        },
        {
            "name": "Alzheimer's Disease",
            "symptoms": ["memory loss", "confusion", "difficulty thinking", "changes in behavior"],
            "doctors": ["Neurologist"]
        },
        {
            "name": "Stroke",
            "symptoms": ["sudden numbness", "confusion", "trouble speaking", "trouble walking"],
            "doctors": ["Neurologist"]
        },
        {
            "name": "Epilepsy",
            "symptoms": ["seizures", "loss of consciousness", "confusion", "muscle spasms"],
            "doctors": ["Neurologist"]
        },
        {
            "name": "Glaucoma",
            "symptoms": ["vision loss", "eye pain", "halos around lights", "redness in the eye"],
            "doctors": ["Ophthalmologist"]
        },
        {
            "name": "Cataracts",
            "symptoms": ["blurry vision", "difficulty seeing at night", "halos around lights", "fading colors"],
            "doctors": ["Ophthalmologist"]
        },
        {
            "name": "Conjunctivitis",
            "symptoms": ["redness in the eye", "itchiness", "tearing", "discharge"],
            "doctors": ["Ophthalmologist"]
        },
        {
            "name": "Tonsillitis",
            "symptoms": ["sore throat", "difficulty swallowing", "fever", "swollen tonsils"],
            "doctors": ["ENT Specialist"]
        },
        {
            "name": "Hemorrhoids",
            "symptoms": ["itching", "bleeding during bowel movements", "pain or discomfort"],
            "doctors": ["Colorectal Surgeon"]
        },
        {
            "name": "Sciatica",
            "symptoms": ["lower back pain", "pain in the buttocks or leg", "numbness", "tingling"],
            "doctors": ["Orthopedist"]
        },
        {
            "name": "Gallstones",
            "symptoms": ["abdominal pain", "back pain", "nausea", "vomiting", "bloating"],
            "doctors": ["Gastroenterologist"]
        },
        {
            "name": "Kidney Stones",
            "symptoms": ["severe pain in the side and back", "painful urination", "blood in urine", "nausea"],
            "doctors": ["Urologist"]
        },
        {
            "name": "Back Pain",
            "symptoms": ["lower back pain", "stiffness", "muscle spasms", "difficulty standing straight"],
            "doctors": ["Orthopedist"]
        },
        {
            "name": "Neck Pain",
            "symptoms": ["stiff neck", "sharp pain", "headaches", "difficulty turning the head"],
            "doctors": ["Orthopedist"]
        },
        {
            "name": "Leg Pain",
            "symptoms": ["pain", "numbness", "tingling", "weakness"],
            "doctors": ["Orthopedist"]
        },
        {
            "name": "Stomachache",
            "symptoms": ["abdominal pain", "cramps", "bloating", "nausea"],
            "doctors": ["General Physician"]
        },
        {
            "name": "Cramps",
            "symptoms": ["muscle cramps", "abdominal cramps", "menstrual cramps", "painful contractions"],
            "doctors": ["General Physician"]
        },
        {
            "name": "Eye Pain",
            "symptoms": ["pain in or around the eye", "redness", "sensitivity to light", "blurred vision"],
            "doctors": ["Ophthalmologist"]
        },
        {
            "name": "Muscle Pain",
            "symptoms": ["muscle soreness", "muscle stiffness", "weakness", "cramps"],
            "doctors": ["General Physician"]
        }
        # Add more diseases here for a larger dataset
    ]
}

# Add more diseases to reach 1000 entries if needed

with open('symptom-disease.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("symptom-disease.json file generated with accurate disease and symptom data including common symptoms.")
