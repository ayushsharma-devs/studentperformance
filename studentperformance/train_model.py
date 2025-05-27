# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv(r"C:\Users\KIIT0001\OneDrive\Desktop\StudentsPerformance.csv")

# Convert categorical variables to numeric
df['gender'] = df['gender'].map({'male': 0, 'female': 1})
df['test preparation course'] = df['test preparation course'].map({'none': 0, 'completed': 1})

# Create average score and pass/fail label
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
df['pass'] = df['average_score'].apply(lambda x: 1 if x >= 50 else 0)

# Select features and labels
X = df[['gender', 'test preparation course']]
y = df['pass']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save model
joblib.dump(model, 'model.pkl')
