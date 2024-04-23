from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from geminiai import get_ai_response, configure_ai
import re
app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/HealthcareDB"
mongo = PyMongo(app)
configure_ai("AIzaSyA_OeuxzXjPyME3Lu5TKY1coJ48VP0pWBw")
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_symptoms = request.form['symptoms']
        condition = match_symptoms(user_symptoms)
        recommended_doctors = recommend_doctors(condition)
        ai_advice = get_ai_response(user_symptoms)
        advice_paragraph = convert_to_paragraph(ai_advice)
        return render_template('results.html', doctors=recommended_doctors, condition=condition, query=user_symptoms,advice=advice_paragraph)
    return render_template('index.html')
def convert_to_paragraph(ai_advice):
    # Remove markdown bold **text**
    advice = re.sub(r'\*\*(.*?)\*\*', r'\1', ai_advice)
    # Replace bullet points: * text
    advice = re.sub(r'\*\s+', '', advice)
    # Remove new lines and excess whitespace
    advice = ' '.join(advice.split())
    return advice
def match_symptoms(user_symptoms):
    symptoms_collection = mongo.db.newsymp
    all_symptoms = list(symptoms_collection.find({}))
    symptoms_texts = [symptom['Symptoms'] for symptom in all_symptoms]
    vectorizer = TfidfVectorizer(stop_words='english')
    symptoms_matrix = vectorizer.fit_transform(symptoms_texts + [user_symptoms])
    similarity_scores = cosine_similarity(symptoms_matrix[-1], symptoms_matrix[:-1]).flatten()
    highest_score_index = similarity_scores.argmax()
    matched_condition = all_symptoms[highest_score_index]['Condition']
    return matched_condition
def recommend_doctors(condition):
    doctors_collection = mongo.db.newdoc
    key_specialty = condition.split('related to')[-1].strip()
    suitable_doctors = list(doctors_collection.find({"Specialty": {'$regex': f'^.*{key_specialty}.*$', '$options': 'i'}}))
    suitable_doctors.sort(key=lambda x: x.get('Rating', 0), reverse=True)
    return suitable_doctors
@app.route('/book/<doctor_name>', methods=['GET'])
def book_appointment_form(doctor_name):
    doctor = mongo.db.doctors.find_one({"Name": doctor_name})
    if not doctor:
        return "Doctor not found", 404
    # Pass doctor availability to the template if needed
    return render_template('book_appointment.html', doctor=doctor)

@app.route('/book/<doctor_name>', methods=['POST'])
def book_appointment(doctor_name):
    patient_name = request.form['patient_name']
    date = request.form['date']
    time = request.form['time']

    doctor = mongo.db.doctors.find_one({"Name": doctor_name})
    if not doctor:
        return "Doctor not found", 404

    # Check for existing appointment at the same time
    existing_appointment = any(appt['date'] == date and appt['time'] == time for appt in doctor.get('Appointments', []))
    if existing_appointment:
        return "This time slot is already booked. Please choose another time."

    # If no conflict, add the new appointment
    new_appointment = {
        'patient_name': patient_name,
        'date': date,
        'time': time
    }
    mongo.db.doctors.update_one({"Name": doctor_name}, {"$push": {"Appointments": new_appointment}})

    # Redirect to the confirmation page
    return redirect(url_for('appointment_confirmation', patient_name=patient_name, doctor_name=doctor_name, date=date, time=time))
@app.route('/appointment_confirmation')
def appointment_confirmation():
    patient_name = request.args.get('patient_name')
    doctor_name = request.args.get('doctor_name')
    date = request.args.get('date')
    time = request.args.get('time')
    return render_template('confirmation.html', patient_name=patient_name, doctor_name=doctor_name, date=date, time=time)
if __name__ == '__main__':
    app.run(debug=True)
