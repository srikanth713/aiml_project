from fastapi import FastAPI
import numpy as np
import joblib

app = FastAPI()

# Load model
model = joblib.load("energy_model.joblib")

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/predict")
def predict(temperature: float, humidity: float, hour: float, appliances: float):
    
    data = np.array([[temperature, humidity, hour, appliances]])
    
    prediction = model.predict(data)
    
    return {"predicted_energy": float(prediction[0])}
