import streamlit as st
import pandas as pd
import joblib

# Load the trained model and scaler
model = joblib.load("sleep_disorder_model.joblib")
scaler = joblib.load("scaler.joblib")

st.set_page_config(page_title="Sleep Disorder Detection", page_icon="😴")

st.title("😴 Sleep Disorder Detection")
st.write("Enter your sleep and lifestyle information to receive a model-based prediction.")

st.warning(
    "Educational project only. This prediction is not a medical diagnosis."
)

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)

gender = st.selectbox("Gender", ["Male", "Female"])

occupation = st.selectbox(
    "Occupation",
    ["Nurse", "Other"]
)

sleep_duration = st.number_input(
    "Average sleep duration (hours)",
    min_value=1.0,
    max_value=14.0,
    value=7.0
)

physical_activity = st.slider(
    "Physical activity level",
    min_value=1,
    max_value=5,
    value=3
)

# Convert slider value to the scale used by the original model
physical_activity = 30 + (physical_activity - 1) * 60 / 4

bmi_category = st.selectbox(
    "BMI category",
    ["Normal", "Overweight"]
)

systolic_bp = st.number_input(
    "Systolic blood pressure",
    min_value=90,
    max_value=200,
    value=120
)

diastolic_bp = st.number_input(
    "Diastolic blood pressure",
    min_value=60,
    max_value=120,
    value=80
)

# Calculate mean arterial pressure
map_value = (systolic_bp + 2 * diastolic_bp) / 3

if st.button("Analyze Sleep Information"):

    # Prepare input using the original model's expected features
    user_data = pd.DataFrame({
        "BMI Category_Normal": [
            1 if bmi_category == "Normal" else 0
        ],
        "BMI Category_Overweight": [
            1 if bmi_category == "Overweight" else 0
        ],
        "Occupation_Nurse": [
            1 if occupation == "Nurse" else 0
        ],
        "Mean Arterial Pressure": [map_value],
        "Sleep Duration": [sleep_duration],
        "Age": [age],
        "Physical Activity Level": [physical_activity],
    })

    continuous_col = [
        "Mean Arterial Pressure",
        "Sleep Duration",
        "Age",
        "Physical Activity Level"
    ]

    binary_col = [
        "BMI Category_Normal",
        "BMI Category_Overweight",
        "Occupation_Nurse"
    ]

    # Standardize continuous features
    user_data_std = scaler.transform(user_data[continuous_col])

    df = pd.DataFrame(
        user_data_std,
        columns=continuous_col
    )

    # Arrange features in the original model's expected order
    df = pd.concat([user_data[binary_col], df], axis=1)

    # Generate prediction
    prediction = int(model.predict(df)[0])

    messages = {
        0: "No sleep disorder predicted by the model.",
        1: "The model predicts a possible risk of sleep apnea.",
        2: "The model predicts a possible risk of insomnia."
    }

    st.subheader("Prediction Result")
    st.info(messages.get(prediction, f"Model returned class: {prediction}"))

    st.caption(
        "This is an experimental machine-learning prediction, "
        "not a confirmed diagnosis. Consult a qualified healthcare "
        "professional about any sleep-related concerns."
    )
