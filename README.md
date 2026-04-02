# Credit Card Fraud Detection System

A machine learning-powered web application that detects fraudulent credit card transactions in real time. Built with **FastAPI**, **Streamlit**, **MySQL**, and **Docker**.

---

## Live Demo

| Service | URL |
|--------|-----|
| Streamlit UI | http://localhost:8501 |
| FastAPI Backend | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |

---

## Features

- Real-time fraud prediction via REST API
- Interactive Streamlit frontend for transaction input
- MySQL database for storing prediction history
- Dockerized setup for easy deployment
- Secure environment variable management

---

## Model Performance

| Metric | Score |
|--------|-------|
| Model | Random Forest Classifier |
| Threshold | 0.8 |
| Precision | 0.8333 |
| Recall | 0.8163 |
| Cross-Validation Score | 0.9765 |

> Precision and Recall are well-balanced, minimizing both false positives and false negatives — critical in fraud detection.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Backend | FastAPI |
| ML Model | Scikit-learn (Random Forest) |
| Database | MySQL 8.0 |
| Containerization | Docker & Docker Compose |
| Data Processing | Pandas, NumPy |

---

## Project Structure

```
Credit_Card_Fraud_Detection_System/
│
├── schema/
│   └── schema.py
│
├── src/
│   ├── components/
│   │   ├── DataIngestion.py
│   │   ├── DataPreprocessing.py
│   │   ├── model_trainer.py
│   │   └── prediction_pipeline.py
│   └── database/
│       ├── connection.py
│       └── operation.py
│
├── Dockerfile.api
├── Dockerfile.frontend
├── docker-compose.yml
├── init.sql
├── main.py
├── trainer_pipeline.py
├── requirements.txt
└── .env.example
```

---

### Prerequisites
- Docker Desktop installed and running
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Riyajangid123/Fraud-Detection-System.git
cd Fraud-Detection-System
```

### 2. Configure Environment Variables
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```env
DB_HOST=mysql_db
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=fraud_db
```

### 3. Run with Docker
```bash
docker-compose up --build
```

### 4. Access the App
- Streamlit UI → http://localhost:8501
- API Docs → http://localhost:8000/docs

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `DB_HOST` | MySQL host (use `mysql_db` for Docker) |
| `DB_USER` | MySQL username |
| `DB_PASSWORD` | MySQL password |
| `DB_NAME` | Database name |

---

## How It Works

1. User inputs transaction details via Streamlit UI
2. Streamlit sends data to FastAPI backend
3. FastAPI runs the data through the trained Random Forest model
4. Prediction (Fraud / Not Fraud) is returned and stored in MySQL
5. Result is displayed on the UI

---

## Author

**Riya Jangid**
- GitHub: [@Riyajangid123](https://github.com/Riyajangid123)