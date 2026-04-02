import joblib
import pandas as pd
from src.database.operation import insert_prediction

class PredictPipeline:
    def __init__(self,model_path="models/model.pkl",threshold=0.8):
        self.model=joblib.load(model_path)
        self.threshold=threshold
    
    def predict(self,transaction:dict):
        df=pd.DataFrame([transaction])
        fraud_prob=self.model.predict_proba(df)[:,1][0]
        prediction=1 if fraud_prob>=self.threshold else 0

        insert_prediction(amount=transaction["Amount"],
                          prediction=prediction)
        
        return{
            "fraud_probability":round(fraud_prob,4),
            "prediction":prediction,
            "status":"FRAUD" if prediction==1 else "LEGIT"
            }