import pandas as pd
from faker import Faker
import random

fake = Faker()

# Define possible values for the fields
specialties = [
    "Pulmonologist",
    "General Physician",
    "Immunologist",
    "Dermatologist",
    "Cardiologist",
    "Neurologist",
    "Gastroenterologist",
    "Endocrinologist",
    "Orthopedist",
    "Oncologist",
    "Psychiatrist",
    "Nephrologist",
    "ENT Specialist",
    "Pediatrician",
    "Rheumatologist",
    "Allergist",
    "Urologist",
    "Ophthalmologist",
    "Podiatrist",
    "Hematologist",
    "Infectious Disease Specialist",
    "Gynecologist",
    "General Surgeon",
    "Emergency Medicine Specialist"
]
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Generate data for 300 doctors
data = []
for _ in range(300):
    name = fake.name()
    specialty = random.choice(specialties)
    availability = random.choice(days_of_week)
    rating = round(random.uniform(3.0, 5.0), 1)  # Ratings between 3.0 and 5.0
    
    data.append({
        'Name': name,
        'Specialty': specialty,
        'Availability': availability,
        'Rating': rating
    })

# Create a DataFrame
df_doctors = pd.DataFrame(data)

# Save to CSV
df_doctors.to_csv('doc_dataset.csv', index=False)
print("Dataset generated and saved to 'doc_dataset.csv'.")
