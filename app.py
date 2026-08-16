# UI for insurance cost prediction

import streamlit as st
import pandas as pd
import joblib

# title
st.title("Medical Insurance Cost Prediction")
st.write("Predict your estimated medical insurance cost using Machine Learning.")

# load trained model
model = joblib.load("model.pkl")

# input fields
age = st.slider("Age", 18, 100, 25)

sex = st.selectbox("Gender", ["female", "male"])

bmi = st.number_input("BMI", 10.0, 50.0, 25.0)

children = st.slider("Number Of Children", 0, 10, 0)

smoker = st.selectbox("Do you smoke?", ["no", "yes"])

region = st.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

# prediction button
if st.button("Predict Insurance Cost"):

    # create dataframe
    input_data = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    # make prediction
    prediction = model.predict(input_data)

    # display result
    st.success("Prediction Complete!")
    st.write("Estimated Insurance Cost")

    st.metric(
        "Insurance Cost",
        f"₹{prediction[0]:,.2f}"
    )