import pandas as pd
from faker import Faker
import random

fake = Faker()

# Define possible values for the fields
specialties = specialists = [
    "general practice",
    "pulmonology",
    "immunology",
    "gastroenterology",
    "nephrology",
    "hematology",
    "urology",
    "endocrinology",
    "ophthalmology",
    "otolaryngology",
    "dermatology",
    "rheumatology",
    "infectious diseases",
    "cardiology",
    "orthopedics",
    "neurology",
    "psychology",
    "pediatrics",
    "oncology",
    "gynecology" 
]

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Generate data for 300 doctors
data = []
for _ in range(400):
    name = fake.name()
    specialty = random.choice(specialties)
    availability = random.choice(days_of_week)
    rating = round(random.uniform(2.0, 5.0), 1)  
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