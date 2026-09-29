import pandas as pd
import streamlit as st
import pickle


df = pd.read_excel('cars24-car-price.xlsx')

st.title("Cars24 Used car Price Prediction")
st.header("Data:")
st.dataframe(df.head())

encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "seller_type": {'Dealer': 1, 'Individual': 2, 'Trustmark Dealer': 3},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

st.header("Prediction:")

col1, col2 = st.columns(2)

with col1:
    fuel_type = st.selectbox("Select the fuel type", ('Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'))

with col2:
    transmission_type = st.selectbox("Select the transmission type:" ,('Manual', 'Automatic'))

col3, col4 = st.columns(2)

with col3:
    engine = st.slider("Set the Engine power", 500, 5000, 1000)

with col4:
    seller_type = st.selectbox("Enter the number of seats",(2, 3, 4, 5, 6, 7, 8, 9, 10))


def model_prediction(fuel_type, transmission_type, engine, seller_type):

    input_features = [[2018.0, 1, 4000, fuel_type, transmission_type, 19.70, engine, 86.30, seller_type]]

    with open("car_pred", "rb") as file:
        reg_model = pickle.load(file)
        return reg_model.predict(input_features)

if st.button("Predict"):

    fuel_type = encode_dict['fuel_type'][fuel_type]
    transmission_type = encode_dict['transmission_type'][transmission_type]

    prediction = model_prediction(fuel_type, transmission_type, engine, seller_type)
    st.write(f"The price of car is {round(prediction[0],2)}.")
