import streamlit as st
import pandas as pd
import joblib

# Ladda pipeline-modellen
model = joblib.load("car_price_model.pkl")

# Ladda options
feature_options = joblib.load("feature_options.pkl")
brand_to_models = joblib.load("brand_to_models.pkl")

st.title("Car Price Prediction")
st.subheader("Fyll i bilens information")

# 1️⃣ Välj Brand
brand = st.selectbox("Brand", feature_options["Brand"])

# 2️⃣ Dynamisk Model-selectbox
models_for_brand = brand_to_models.get(brand, [])
model_name = st.selectbox("Model", models_for_brand)

# Övriga inputs
fuel_type = st.selectbox("Fuel Type", feature_options["Fuel_Type"])
transmission = st.selectbox("Transmission", feature_options["Transmission"])
year = st.number_input("Year", 1990, 2025, 2020)
engine_size = st.number_input("Engine Size", 0.8, 6.0, 2.0)
mileage = st.number_input("Mileage", 0, 500000, 10000)
doors = st.number_input("Doors", 2, 5, 4)
owner_count = st.number_input("Owner Count", 1, 10, 1)

# Skapa DataFrame för prediktion
input_data = pd.DataFrame([{
    "Brand": brand,
    "Model": model_name,
    "Year": year,
    "Engine_Size": engine_size,
    "Fuel_Type": fuel_type,
    "Transmission": transmission,
    "Mileage": mileage,
    "Doors": doors,
    "Owner_Count": owner_count
}])

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: {prediction[0]:,.0f} SEK")