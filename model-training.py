import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


data = {
    "vibration": np.random.uniform(0.5, 3.0, 1000),  
    "temperature": np.random.uniform(30, 80, 1000),  
    "failure": np.random.choice([0, 1], 1000, p=[0.8, 0.2])  
}

df = pd.DataFrame(data)


X = df.drop("failure", axis=1)
y = df["failure"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


joblib.dump(model, 'predictive_maintenance_model.pkl')

print("Model trained and saved as 'predictive_maintenance_model.pkl'")
