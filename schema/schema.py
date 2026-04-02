from pydantic import BaseModel

class Transaction(BaseModel):
    Time: float
    Amount: float
    V1: float = 0.0
    V2: float = 0.0
    V3: float = 0.0
    V4: float = 0.0
    V5: float = 0.0
    V6: float = 0.0
    V7: float = 0.0
    V8: float = 0.0
    V9: float = 0.0
    V10: float = 0.0
    V11: float = 0.0
    V12: float = 0.0
    V13: float = 0.0
    V14: float = 0.0
    V15: float = 0.0
    V16: float = 0.0
    V17: float = 0.0
    V18: float = 0.0
    V19: float = 0.0
    V20: float = 0.0
    V21: float = 0.0
    V22: float = 0.0
    V23: float = 0.0
    V24: float = 0.0
    V25: float = 0.0
    V26: float = 0.0
    V27: float = 0.0
    V28: float = 0.0

    class Config:
        json_schema_extra = {
            "example": {
                "Time": 1000.0,
                "Amount": 149.62,
                "V1": -1.35,
                "V2": -0.07,
                "V3": 2.53,
                "V4": 1.37,
                "V5": -0.33,
                "V6": 0.46,
                "V7": 0.23,
                "V8": 0.09,
                "V9": 0.36,
                "V10": 0.09,
                "V11": -0.55,
                "V12": -0.61,
                "V13": -0.99,
                "V14": -0.31,
                "V15": 1.46,
                "V16": -0.47,
                "V17": 0.20,
                "V18": 0.02,
                "V19": 0.40,
                "V20": 0.25,
                "V21": -0.01,
                "V22": 0.27,
                "V23": -0.11,
                "V24": 0.06,
                "V25": 0.12,
                "V26": -0.18,
                "V27": 0.13,
                "V28": -0.02
            }
        }