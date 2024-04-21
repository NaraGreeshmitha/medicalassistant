import json
import google.generativeai as genai
from pymongo import MongoClient
genai.configure(api_key="AIzaSyA_OeuxzXjPyME3Lu5TKY1coJ48VP0pWBw")
model = genai.GenerativeModel('gemini-pro')
text='''i have these cateogory of doctors
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
    "Emergency Medicine Specialist" suggest me best doctors based on the symptoms "cold" give me output in this format {
  "recommended_doctors": [
    {
      "category": "",
      "reason": ""
    },
    {
      "category": "",
      "reason": ""
    }
  ]
}
'''
response = model.generate_content(text)
result = response._result.candidates[0].content.parts[0].text
json_data = result.strip('```json\n').strip('\n```')
print(json_data)
try:
    response_json = json.loads(json_data)
    recommended_specialties = [item['category'] for item in response_json["recommended_doctors"]]
except (json.JSONDecodeError, KeyError) as e:
    print("Error parsing JSON or accessing keys:", e)
    exit()

# MongoDB Setup
client = MongoClient('mongodb://localhost:27017/')
db = client['HealthcareDB']
collection = db['doctors']

# Function to find top doctors
def find_top_doctors(specialties):
    top_doctors = []
    for specialty in specialties:
        top_doc = collection.find_one(
            {'Specialty': {'$regex': f'^{specialty}$', '$options': 'i'}},
            sort=[('Rating', -1)]
        )
        if top_doc:
            top_doctors.append(top_doc)
    return top_doctors

# Retrieve and print top doctors
top_doctors = find_top_doctors(recommended_specialties)
if top_doctors:
    for doctor in top_doctors:
        print(f"Name: {doctor['Name']}, Specialty: {doctor['Specialty']}, Rating: {doctor['Rating']}")
else:
    print("No top doctors found for the given specialties.")