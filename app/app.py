import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import joblib
import numpy as np
from src.data_preprocessing import load_and_preprocess_data

st.title("Osteoporosis Stage Predictor")

# Gender selection
gender = st.selectbox("Select Gender", ["Men", "Women"])

age = st.slider("Age", 40, 90)
bmi = st.number_input("BMI", value=25.0)
testosterone = st.number_input("Testosterone Level (ng/dL)", value=600.0 if gender == "Men" else 50.0)
vitamin_d = st.number_input("Vitamin D Level (ng/mL)", value=25.0)
calcium = st.number_input("Calcium Intake (mg/day)", value=800.0)
alcohol = st.slider("Alcohol Intake (drinks/week)", 0, 10)
smoking = st.selectbox("Smoking", ["No", "Yes"])
physical = st.slider("Physical Activity Level (1 - Low to 5 - High)", 1, 5)

# Predict button
if st.button("Predict Stage"):
    try:
        # Load model
        model = joblib.load(f"model_{gender}.pkl")

        # Load scaler (refit it from data_preprocessing)
        _, _, _, _, scaler = load_and_preprocess_data(gender)

        # Prepare input
        input_data = np.array([[age, bmi, testosterone, vitamin_d, calcium,
                                alcohol, 1 if smoking == "Yes" else 0, physical]])

        input_scaled = scaler.transform(input_data)

        # Prediction
        prediction = model.predict(input_scaled)[0]

        stage_map = {
            0: "Normal",
            1: "Osteopenia",
            2: "Osteoporosis",
            3: "Severe Osteoporosis"
        }

        # st.success(f"Predicted Stage: {stage_map[prediction]}")
        st.markdown(f"<h2 style='text-align: center; color: green;'> {stage_map[prediction]}</h2>", unsafe_allow_html=True)


    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
