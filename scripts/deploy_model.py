from fastapi import FastAPI
import xgboost as xgb
import numpy as np
import json

app = FastAPI()

model = xgb.Booster()
model.load_model("models/fraud_model.json")

@app.post("/predict")
async def predict(request: dict):
    data = np.array([request["features"]])
    prediction = model.predict(xgb.DMatrix(data))
    return {"fraud_prediction": int(prediction[0])}

