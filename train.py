#code which is runned in google colab to train and build a model for the given dataset and save it as .h5 file .The saved files are imported into vscode 
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model
# Load the dataset
data = pd.read_csv('symptoms_dataset.csv')

# Split the 'Symptoms' into a list
data['Symptoms'] = data['Symptoms'].apply(lambda x: x.split(','))

# Creating a set of all unique symptoms
all_symptoms = set(x for sublist in data['Symptoms'] for x in sublist)
symptom_index = {symptom: idx for idx, symptom in enumerate(all_symptoms)}

# Function to encode list of symptoms into a binary format
def encode_symptoms(symptoms):
    encoding = np.zeros(len(symptom_index))
    for symptom in symptoms:
        encoding[symptom_index[symptom]] = 1
    return encoding

# Apply encoding to each entry
X = np.array([encode_symptoms(symptoms) for symptoms in data['Symptoms']])

# Encoding the conditions using LabelEncoder and converting to categorical
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['Condition'])
y = to_categorical(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = Sequential([
    Dense(128, input_shape=(len(symptom_index),), activation='relu'),
    Dense(64, activation='relu'),
    Dense(y.shape[1], activation='softmax')  # Output layer with a softmax activation
])

# Compiling the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Display model architecture
model.summary()
model.fit(X_train, y_train, epochs=10000, batch_size=80, validation_split=0.1)
model.save('my_saved_modelll')  # saves to a TensorFlow SavedModel format
print("Model saved successfully in SavedModel format.")
model = load_model('my_saved_modelll')
print("Model loaded successfully from SavedModel format.")
def predict_condition(symptoms):
    symptoms_list = symptoms.split(',')  # Assuming input as a comma-separated string
    symptoms_encoded = encode_symptoms(symptoms_list)
    symptoms_encoded = np.array([symptoms_encoded])  # Reshape for model input
    prediction = model.predict(symptoms_encoded)
    predicted_index = np.argmax(prediction)
    predicted_condition = label_encoder.inverse_transform([predicted_index])
    return predicted_condition[0]

# Example prediction
test_symptoms = "muscle pain, morning stiffness"
predicted_condition = predict_condition(test_symptoms)
print(f"Predicted condition for symptoms '{test_symptoms}': {predicted_condition}")
with open('label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

with open('symptom_index.pkl', 'wb') as f:
    pickle.dump(symptom_index, f)