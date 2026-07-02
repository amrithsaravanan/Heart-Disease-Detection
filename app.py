import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Heart Disease Prediction using KNN")
st.write("Enter the patient's details below and click **Predict**.")

# -----------------------------
# Load Model and Scaler
# -----------------------------
with open("models/knn_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.markdown("---")

# -----------------------------
# User Inputs
# -----------------------------

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=45
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)
sex = 0 if gender == "Female" else 1

chest_pain = st.selectbox(
    "Chest Pain Type",
    [
        "Typical Angina",
        "Atypical Angina",
        "Non-anginal Pain",
        "Asymptomatic"
    ]
)
cp = [
    "Typical Angina",
    "Atypical Angina",
    "Non-anginal Pain",
    "Asymptomatic"
].index(chest_pain)

trestbps = st.number_input(
    "Resting Blood Pressure (mm Hg)",
    min_value=80,
    max_value=250,
    value=120
)

chol = st.number_input(
    "Serum Cholesterol (mg/dL)",
    min_value=100,
    max_value=600,
    value=200
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dL",
    ["No", "Yes"]
)
fbs = 0 if fbs == "No" else 1

restecg = st.selectbox(
    "Resting ECG Result",
    [
        "Normal",
        "ST-T Wave Abnormality",
        "Left Ventricular Hypertrophy"
    ]
)
restecg = [
    "Normal",
    "ST-T Wave Abnormality",
    "Left Ventricular Hypertrophy"
].index(restecg)

thalach = st.number_input(
    "Maximum Heart Rate Achieved",
    min_value=60,
    max_value=250,
    value=150
)

exang = st.selectbox(
    "Exercise Induced Angina",
    ["No", "Yes"]
)
exang = 0 if exang == "No" else 1

oldpeak = st.number_input(
    "ST Depression",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    [
        "Upsloping",
        "Flat",
        "Downsloping"
    ]
)
slope = [
    "Upsloping",
    "Flat",
    "Downsloping"
].index(slope)

ca = st.selectbox(
    "Number of Major Vessels",
    [0, 1, 2, 3, 4]
)

thal = st.selectbox(
    "Thalassemia",
    [
        "Normal",
        "Fixed Defect",
        "Reversible Defect"
    ]
)

thal = {
    "Normal": 1,
    "Fixed Defect": 2,
    "Reversible Defect": 3
}[thal]

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

    input_data = pd.DataFrame([[
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]], columns=[
        "age",
        "sex",
        "cp",
        "trestbps",
        "chol",
        "fbs",
        "restecg",
        "thalach",
        "exang",
        "oldpeak",
        "slope",
        "ca",
        "thal"
    ])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    st.markdown("---")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ No Heart Disease Detected")

    st.subheader("Patient Details")

    st.dataframe(input_data)

st.markdown("---")
st.caption("Heart Disease Prediction System using K-Nearest Neighbors (KNN)")