import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# ----------------------------------------------------
# 1. LOAD & PREPARE DATA
# ----------------------------------------------------

# Read directly from the file you saved locally
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigree', 'Age', 'Outcome']
data = pd.read_csv('diabetes.csv', names=columns)

# Split into Features (X) and Target (y)
X = data.drop(columns=['Outcome'])
y = data['Outcome']

# ----------------------------------------------------
# 2. TRAIN-TEST SPLIT
# ----------------------------------------------------
# Reserve 20% of data for evaluating the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ----------------------------------------------------
# 3. FEATURE SCALING (Data Preprocessing)
# ----------------------------------------------------
# Normalize the scale of features so large values don't dominate the algorithm
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ----------------------------------------------------
# 4. MODEL SELECTION & TRAINING
# ----------------------------------------------------
# We initialize a Random Forest Classifier and fit (train) it on the data
#model = RandomForestClassifier(random_state=42, n_estimators=100)
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# ----------------------------------------------------
# 5. MODEL EVALUATION & PREDICTION
# ----------------------------------------------------
# Use the trained model to predict outcomes on the unseen test set
predictions = model.predict(X_test_scaled)

# Calculate accuracy percentage
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%\n")
print("Detailed Classification Report:")
print(classification_report(y_test, predictions))

# ----------------------------------------------------
# 6. MAKING A NEW PREDICTION
# ----------------------------------------------------

# Fixed the name here to match what your scaler expects
feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigree', 'Age']

# Dummy data for a new patient
new_patient = [[2, 130, 70, 25, 0, 28.1, 0.35, 33]]

# Convert the list to a DataFrame with the corrected column names
new_patient_df = pd.DataFrame(new_patient, columns=feature_names)

# Scale and predict
new_patient_scaled = scaler.transform(new_patient_df)
prediction = model.predict(new_patient_scaled)

result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"
print(f"Prediction for new patient: {result}")
