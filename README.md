# Doctor Recommendation System
## Overview
The Doctor Recommendation System is a web-based application designed to assist patients in finding appropriate healthcare providers based on their symptoms. Using Python, Flask, scikit-learn, pandas, and Flask-PyMongo, this application integrates a machine learning model to suggest the most relevant doctors stored in a MongoDB database.
## Features
- **Symptom Input:** Users can enter their health symptoms into a user-friendly interface.
- **Doctor Recommendations:** Based on the input symptoms, the system recommends doctors specializing in the relevant medical fields.
- **Database Integration:** Utilizes MongoDB for storing and retrieving doctor information and patient queries.
- **Time Slot Selection and Booking:** Users can select a time slot for an appointment with a recommended doctor. The system checks the 
    availability of the selected time slot in real-time and, if available, books it for the user.
- **Generative AI Integration:**  Uses Gemini AI API to generate safety precautions to be taken by user for temporary     relief before patient visits the doctor.

## Requirements
- Python 3.8+
- Flask
- scikit-learn
- pandas
- Flask-PyMongo
- MongoDB
- Tensorflow
- Numpy
- Keras

## Installation

### Clone the repository
```bash
git clone https://github.com/NaraGreeshmitha/medicalassistant.git
cd medicalassistant
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Configure and Populate MongoDB
- Ensure MongoDB is installed and running on your system.
- Create a database named HealthcareDB.
- Import the datasets
- Run the following commands to import your data into MongoDB. Ensure you replace path\to\symptoms_dataset.csv and path\to\doc_dataset.csv with the actual paths to your data files.
 ```bash
mongoimport --type csv --headerline --file path\to\symptoms_dataset.csv --collection newsymp --db HealthcareDB
mongoimport --type csv --headerline --file path\to\doc_dataset.csv --collection newdoc --db HealthcareDB
```
## Usage
- start mongodb server
```bash
mongosh
```
### Running the application
```bash
python app.py
```
Navigate to `http://127.0.0.1:5000/` in your web browser to start using the application.

### Using the application
- On the homepage, enter the symptoms you are experiencing in the provided form.
- Submit the form to see the list of recommended doctors along with their specialties and advice given by the generative AI
- Book the appointment by clicking on book appointment.
- You will be redirected to page where patient has to fill their details and book the appointment at particular date and time.
  
## Contact
- Your Name - nara greeshmitha
- Email id: naragreeshmitha123@gmail.com
