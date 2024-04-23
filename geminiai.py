import json
import google.generativeai as genai
from pymongo import MongoClient
def configure_ai(api_key):
    genai.configure(api_key=api_key)
def get_ai_response(symptoms):
    model = genai.GenerativeModel('gemini-pro')
    text=f"Based on the symptom '{symptoms}', suggest first aid or safety measures for temporary relief for the patient before reaching a doctor."
    response = model.generate_content(text)
    advice = response._result.candidates[0].content.parts[0].text.strip('```json\n').strip('\n```')
    return advice
    # result = response._result.candidates[0].content.parts[0].text
    # json_data = result.strip('```json\n').strip('\n```')
    # print(json_data)
# client = MongoClient('mongodb://localhost:27017/')
# db = client['HealthcareDB']
# collection = db['doctors']
# response_json = json.loads(json_data)
# try:
#     response_json = json.loads(json_data)
#     recommended_specialties = [item['category'] for item in response_json["recommended_doctors"]]
# except (json.JSONDecodeError, KeyError) as e:
#     print("Error parsing JSON or accessing keys:", e)
#     exit()

# # MongoDB Setup
# client = MongoClient('mongodb://localhost:27017/')
# db = client['HealthcareDB']
# collection = db['doctors']

# # Function to find top doctors
# def find_top_doctors(specialties):
#     top_doctors = []
#     for specialty in specialties:
#         top_doc =collection.find({"Specialty": {'$regex': f'^.*{specialty}.*$', '$options': 'i'}})
#         if top_doc:
#             top_doctors.append(top_doc)
#     return top_doctors

# # Retrieve and print top doctors
# top_doctors = find_top_doctors(recommended_specialties)
# print(top_doctors)
# if top_doctors:
#     for doctor in top_doctors:
#         print(f"Name: {doctor['Name']}, Specialty: {doctor['Specialty']}, Rating: {doctor['Rating']}")
# else:
#     print("No top doctors found for the given specialties.")