import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Sleep Disorder Detection",
    page_icon="😴",
    layout="centered"
)

st.title("😴 Sleep Disorder Detection")
st.write(
    "Enter your sleep and lifestyle information "
    "to explore a machine-learning prediction."
)

st.warning(
    "Educational project only. This application does not "
    "provide a medical diagnosis."
)

st.header("Personal Information")

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=25
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

occupation = st.selectbox(
    "Occupation",
    [
        "Student",
        "Software Engineer",
        "Doctor",
        "Nurse",
        "Teacher",
        "Other"
    ]
)

st.header("Sleep Information")

sleep_duration = st.slider(
    "Average sleep duration (hours)",
    1.0,
    14.0,
    7.0,
    0.5
)

quality_of_sleep = st.slider(
    "Sleep quality (1 = poor, 10 = excellent)",
    1,
    10,
    7
)

physical_activity = st.slider(
    "Physical activity level",
    0,
    100,
    50
)

stress_level = st.slider(
    "Stress level (1 = low, 10 = high)",
    1,
    10,
    5
)

st.header("Health Information")

bmi_category = st.selectbox(
    "BMI category",
    ["Normal", "Overweight", "Obese"]
)

systolic_bp = st.number_input(
    "Systolic blood pressure",
    min_value=70,
    max_value=250,
    value=120
)

diastolic_bp = st.number_input(
    "Diastolic blood pressure",
    min_value=40,
    max_value=150,
    value=80
)

if st.button("Analyze Sleep Information"):
    st.subheader("Your Submitted Information")

    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    st.write(f"Occupation: {occupation}")
    st.write(f"Sleep duration: {sleep_duration} hours")
    st.write(f"Sleep quality: {quality_of_sleep}/10")
    st.write(f"Physical activity: {physical_activity}")
    st.write(f"Stress level: {stress_level}/10")
    st.write(f"BMI category: {bmi_category}")
    st.write(
        f"Blood pressure: {systolic_bp}/{diastolic_bp}"
    )

    st.info(
        "Your information has been collected successfully. "
        "A trained prediction model must be connected before "
        "this application can produce a machine-learning prediction."
    )
