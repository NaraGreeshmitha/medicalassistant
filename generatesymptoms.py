import pandas as pd
from faker import Faker
import random

fake = Faker()

# Define possible symptoms associated with each specialty
symptoms_by_specialty = {
    'Cardiology': ['chest pain', 'shortness of breath', 'dizziness'],
    'Dermatology': ['rash', 'itching', 'redness'],
    'Neurology': ['headache', 'numbness', 'memory loss'],
    'Pediatrics': ['fever', 'cough', 'vomiting'],
    'Orthopedics': ['joint pain', 'swelling', 'limited mobility'],
    'Oncology': ['lumps', 'weight loss', 'fatigue'],
    'Gastroenterology': ['abdominal pain', 'bloating', 'diarrhea'],
    'Endocrinology': ['fatigue', 'mood swings', 'weight change'],
    'General Practice': ['fever', 'headache', 'tiredness']
}

# Generate data
data = []
for specialty, symptoms_list in symptoms_by_specialty.items():
    for _ in range(25):  # Adjust the number to generate more or fewer records per specialty
        condition = fake.word(ext_word_list=['disease', 'disorder', 'syndrome'])
        full_condition = f"{condition} related to {specialty.lower()}"
        symptoms = random.sample(symptoms_list, min(2, len(symptoms_list)))  # Pick 2 symptoms randomly
        data.append({
            'Condition': full_condition,
            'Symptoms': ', '.join(symptoms)
        })

# Create a DataFrame
df_symptoms = pd.DataFrame(data)

# Save to CSV
df_symptoms.to_csv('symptoms_dataset.csv', index=False)
print("Symptoms dataset generated and saved to 'symptoms_dataset.csv'.")
