from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import joblib
from main import app


# Mock model before importing app
mock_model = MagicMock()
mock_model.predict_proba.return_value = [[0.2, 0.8]]

# Patch joblib.load before importing main
joblib.load = lambda x: mock_model


client = TestClient(app)

client = TestClient(app) #testclient checks that without running the app it test in python

sample_transaction = {
    "Time": 1000.0,
    "Amount": 149.62,
    "V1": -1.35, "V2": -0.07, "V3": 2.53, "V4": 1.37,
    "V5": -0.33, "V6": 0.46, "V7": 0.23, "V8": 0.09,
    "V9": 0.36, "V10": 0.09, "V11": -0.55, "V12": -0.61,
    "V13": -0.99, "V14": -0.31, "V15": 1.46, "V16": -0.47,
    "V17": 0.20, "V18": 0.02, "V19": 0.40, "V20": 0.25,
    "V21": -0.01, "V22": 0.27, "V23": -0.11, "V24": 0.06,
    "V25": 0.12, "V26": -0.18, "V27": 0.13, "V28": -0.02
}

#Checking that home endpoint is alive or not
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Fraud Detection System"}


# Predict endpoint returns correct response structure
@patch("main.insert_prediction")  # mock DB so no real DB needed during testing for faster execution
def test_predict_returns_correct_structure(mock_insert):
    mock_insert.return_value = None
    response = client.post("/predict", json=sample_transaction)
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "fraud_probability" in data
    assert "amount" in data


# Status is either FRAUD or LEGIT
@patch("main.insert_prediction")
def test_predict_status_values(mock_insert):
    mock_insert.return_value = None
    response = client.post("/predict", json=sample_transaction)
    assert response.status_code == 200
    assert response.json()["status"] in ["FRAUD", "LEGIT"]


# Amount in response matches input
@patch("main.insert_prediction")
def test_predict_amount_matches(mock_insert):
    mock_insert.return_value = None
    response = client.post("/predict", json=sample_transaction)
    assert response.status_code == 200
    assert response.json()["amount"] == sample_transaction["Amount"]


# Missing required fields returns 422
def test_predict_missing_fields():
    response = client.post("/predict", json={"Amount": 100.0})  # missing Time
    assert response.status_code == 422


# Fraud probability is between 0 and 1
@patch("main.insert_prediction")
def test_fraud_probability_range(mock_insert):
    mock_insert.return_value = None
    response = client.post("/predict", json=sample_transaction)
    prob = response.json()["fraud_probability"]
    assert 0.0 <= prob <= 1.0