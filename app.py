import streamlit as st
import pandas as pd
import pickle

dataset = pd.read_csv("insurance.csv")
model = pickle.load(open('linear.pkl', 'rb'))

# Function to predict medical costs
def predict_medical_cost(data):
    prediction = model.predict(data)
    return prediction

# Function to display the web app interface
def display_interface():
    st.title("Medical Cost Prediction")

    st.write("Enter the following information to predict medical costs for a person:")

    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    sex = st.selectbox("Sex", ["Male", "Female"])
    bmi = st.number_input("BMI", min_value=10.0, max_value=55.5, value=25.0)
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
    smoker = st.selectbox("Smoker", ["No", "Yes"])
    region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

    sex_encoded = 0 if sex == "Male" else 1
    smoker_encoded = 1 if smoker == "Yes" else 0
    region_encoded = ['Northeast', 'Northwest', 'Southeast', 'Southwest'].index(region)

    data = pd.DataFrame([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]],
                        columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

    if st.button("Predict"):
        prediction = predict_medical_cost(data)
        st.write("Predicted Medical Cost: $", round(prediction[0]))

# Run the web app
if __name__ == '__main__':
    display_interface()
