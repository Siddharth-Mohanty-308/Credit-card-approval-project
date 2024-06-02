import streamlit as st
import joblib
import numpy as np

# Load the pre-trained model
try:
    model = joblib.load('decision_tree.joblib')
except FileNotFoundError:
    st.error('Model file not found. Please ensure the model is available.')

st.title('Credit Card Approval Prediction')

# Create a form
with st.form('credit_form'):
    st.header('Enter your details:')
    reports = st.number_input('Number of Reports', min_value=0, step=1, format='%d')
    age = st.slider('Age', min_value=18, max_value=95, step=1)
    income = st.number_input('Yearly Income', min_value=0, step=1000, format='%d')
    expenses = st.number_input('Monthly Card Expenses', min_value=0, step=100, format='%d')
    house_owner = st.selectbox('Owner of House', options=[(1, 'Yes'), (0, 'No')], format_func=lambda x: x[1])[0]
    self_employed = st.selectbox('Self Employed', options=[(1, 'Yes'), (0, 'No')], format_func=lambda x: x[1])[0]
    dependents = st.number_input('Number of Dependents', min_value=0, step=1, format='%d')
    months_address = st.number_input('Months Lived in Current Address', min_value=0, step=1, format='%d')
    major_cards = st.number_input('Number of Major Cards', min_value=0, step=1, format='%d')
    credit_accounts = st.number_input('Active Credit Accounts', min_value=0, step=1, format='%d')
    
    submitted = st.form_submit_button('Submit')

if submitted:
    if 'model' in locals():
        try:
            # Prepare data for prediction
            features = np.array([[reports, age, income, expenses, house_owner, self_employed, dependents, months_address, major_cards, credit_accounts]])
            
            # Make prediction
            prediction = model.predict(features)[0]
            
            # Determine the result message
            if prediction == 1:
                result = "Credit Card Approved"
            else:
                result = "Credit Card Not Approved"
            
            st.subheader(result)
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.error("Model is not loaded. Please check the model file.")


