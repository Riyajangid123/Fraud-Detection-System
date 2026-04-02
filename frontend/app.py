import streamlit as st
import requests

st.set_page_config(page_title="Fraud Detection System", layout="centered")

st.title("Fraud Detection System")
st.write("Predict whether a credit card transaction is fraudulent")
st.markdown("---")

Time = st.number_input("Time (seconds elapsed since first transaction)", min_value=0.0)

st.subheader("PCA Features (V1 – V14)")
col1, col2, col3, col4 = st.columns(4)
with col1:
    V1  = st.number_input("V1",  value=0.0, format="%.4f")
    V5  = st.number_input("V5",  value=0.0, format="%.4f")
    V9  = st.number_input("V9",  value=0.0, format="%.4f")
    V13 = st.number_input("V13", value=0.0, format="%.4f")
with col2:
    V2  = st.number_input("V2",  value=0.0, format="%.4f")
    V6  = st.number_input("V6",  value=0.0, format="%.4f")
    V10 = st.number_input("V10", value=0.0, format="%.4f")
    V14 = st.number_input("V14", value=0.0, format="%.4f")
with col3:
    V3  = st.number_input("V3",  value=0.0, format="%.4f")
    V7  = st.number_input("V7",  value=0.0, format="%.4f")
    V11 = st.number_input("V11", value=0.0, format="%.4f")
with col4:
    V4  = st.number_input("V4",  value=0.0, format="%.4f")
    V8  = st.number_input("V8",  value=0.0, format="%.4f")
    V12 = st.number_input("V12", value=0.0, format="%.4f")

st.subheader("PCA Features (V15 – V28)")
col5, col6, col7, col8 = st.columns(4)
with col5:
    V15 = st.number_input("V15", value=0.0, format="%.4f")
    V19 = st.number_input("V19", value=0.0, format="%.4f")
    V23 = st.number_input("V23", value=0.0, format="%.4f")
    V27 = st.number_input("V27", value=0.0, format="%.4f")
with col6:
    V16 = st.number_input("V16", value=0.0, format="%.4f")
    V20 = st.number_input("V20", value=0.0, format="%.4f")
    V24 = st.number_input("V24", value=0.0, format="%.4f")
    V28 = st.number_input("V28", value=0.0, format="%.4f")
with col7:
    V17 = st.number_input("V17", value=0.0, format="%.4f")
    V21 = st.number_input("V21", value=0.0, format="%.4f")
    V25 = st.number_input("V25", value=0.0, format="%.4f")
with col8:
    V18 = st.number_input("V18", value=0.0, format="%.4f")
    V22 = st.number_input("V22", value=0.0, format="%.4f")
    V26 = st.number_input("V26", value=0.0, format="%.4f")

st.subheader("Transaction Details")
Amount = st.number_input("Amount ($)", min_value=0.0, value=0.0)

st.markdown("---")

if st.button("Analyze Transaction"):

    url = "http://fraud_api:8000/predict"

    payload = {
        "Time": Time,
        "V1": V1,   "V2": V2,   "V3": V3,   "V4": V4,
        "V5": V5,   "V6": V6,   "V7": V7,   "V8": V8,
        "V9": V9,   "V10": V10, "V11": V11, "V12": V12,
        "V13": V13, "V14": V14, "V15": V15, "V16": V16,
        "V17": V17, "V18": V18, "V19": V19, "V20": V20,
        "V21": V21, "V22": V22, "V23": V23, "V24": V24,
        "V25": V25, "V26": V26, "V27": V27, "V28": V28,
        "Amount": Amount
    }

    response = requests.post(url, json=payload, timeout=10)

    if response.status_code == 200:
        result = response.json()

        st.markdown("## Results")

        # Fraud result
        if result["status"] == "FRAUD":
            st.error("Fraudulent Transaction Detected")
        else:
            st.success("Transaction Appears Legitimate")

        # Probability
        st.info(f"Fraud Probability: {result['fraud_probability']:.2%}")

    else:
        st.error("Error connecting to API")
