from fastapi import FastAPI,HTTPException
import joblib
from schema.schema import Transaction
import pandas as pd
from src.database.operation import insert_prediction, fetch_all_predictions


app = FastAPI(
    title="Fraud Detection System",
    description="Detects fraudulent credit card transactions",
    version="1.0.0"
)
model=joblib.load("models/model.pkl")
threshold=0.8

@app.get("/")
def home():
    return {"message":"Welcome to Fraud Detection System"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data:Transaction):
    try:
        input_data=pd.DataFrame([data.model_dump()])

        fraud_prob=model.predict_proba(input_data)[:,1][0]
        prediction = 1 if fraud_prob >= threshold else 0

        insert_prediction(
            amount=data.Amount,
            prediction=prediction
        )

        return {
                "status": "FRAUD" if prediction == 1 else "LEGIT",
                "fraud_probability": round(float(fraud_prob), 4),
                "amount": data.Amount
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




