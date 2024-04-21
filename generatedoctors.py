import pandas as pd
from faker import Faker
import random

fake = Faker()

# Define possible values for the fields
specialties = ['Cardiology', 'Dermatology', 'Neurology', 'Pediatrics', 'Orthopedics',
               'Oncology', 'Gastroenterology', 'Endocrinology', 'General Practice']
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Generate data for 200 doctors
data = []
for _ in range(200):
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
df_doctors.to_csv('doctors_dataset.csv', index=False)
print("Dataset generated and saved to 'doctors_dataset.csv'.")
