import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# 1. Create a dummy dataset (Features: Glucose, BMI, Age -> Target: Outcome)
data = {
    'Glucose': [120, 140, 130, 150, 110, 160, 125, 170],
    'BMI': [22.1, 33.4, 24.0, 38.2, 21.5, 30.1, 26.3, 31.0],
    'Age': [25, 50, 35, 60, 22, 45, 30, 55],
    'Outcome': [0, 1, 0, 1, 0, 1, 0, 1]  # 0 = Non-Diabetic, 1 = Diabetic
}
df = pd.DataFrame(data)

# 2. Separate features (X) and target label (y)
X = df[['Glucose', 'BMI', 'Age']]
y = df['Outcome']

# 3. Split the data into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# 4. Scale the features (important for many classification models)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Initialize and Train the Classification Model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)

# Calculate accuracy percentage
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy * 100:.2f}%\n")
print("Detailed Classification Report:")
print(classification_report(y_test, predictions))

# 6. Predict on a brand new patient
# Creating a DataFrame to ensure feature names match perfectly
new_patient = pd.DataFrame([[130, 28.1, 33]], columns=['Glucose', 'BMI', 'Age'])
new_patient_scaled = scaler.transform(new_patient)

# Make the classification prediction
prediction = model.predict(new_patient_scaled)

# Display the classification result
result = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"
print(f"Classification Prediction: {result}")