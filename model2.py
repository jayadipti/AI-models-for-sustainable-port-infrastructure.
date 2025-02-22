import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Generate simulated dataset with vibration and temperature as features
data = {
    "vibration": np.random.uniform(0.5, 3.0, 1000),  # Vibration levels
    "temperature": np.random.uniform(30, 80, 1000),  # Temperature readings
    "failure": np.random.choice([0, 1], 1000, p=[0.8, 0.2])  # 80% no failure, 20% failure
}

df = pd.DataFrame(data)

# Split dataset into features and target
X = df.drop("failure", axis=1)
y = df["failure"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'predictive_maintenance_model.pkl')

print("Model trained and saved as 'predictive_maintenance_model.pkl'")
