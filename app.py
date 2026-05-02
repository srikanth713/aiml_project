from fastapi import FastAPI
import numpy as np
import joblib

from schemas import InputData   # 👈 import from new file

app = FastAPI()

model = joblib.load("smart_home_energy_model.joblib")

@app.post("/predict")
def predict(data: InputData):
    input_data = np.array([[data.temperature, data.humidity, data.hour]])
    
    result = model.predict(input_data)
    
    return {"predicted_energy": float(result[0])}
