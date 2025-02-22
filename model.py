import numpy as np
import joblib
import time


model = joblib.load("predictive_maintenance_model.pkl")


def get_sensor_data():
    vibration = np.random.uniform(0.5, 3.0)  
    temperature = np.random.uniform(30, 80) 
    return vibration, temperature


for i in range(10): 
    vibration, temperature = get_sensor_data()
    
    
    features = np.array([[vibration, temperature]])

    
    failure_risk = model.predict(features)

    
    if failure_risk[0] == 1:
        print(f"Test {i+1}: ⚠️ High Risk | Vibration: {vibration:.2f}, Temp: {temperature:.2f}")
    else:
        print(f"Test {i+1}: ✅ Low Risk | Vibration: {vibration:.2f}, Temp: {temperature:.2f}")

    time.sleep(1) 