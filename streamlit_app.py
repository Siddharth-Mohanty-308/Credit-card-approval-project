#'months_in_current_address',
# 'active_credit_accounts'

import streamlit as st
import numpy as np
import joblib

model=joblib.load('decision_tree_model.joblib')

st.title("Credit Card Approval Prediction")

with st.form('Details Form'):
    reports=st.number_input("Number of Reports:", min_value=0, step=1, format='%d')
    age=st.slider("Age:", min_value=18, max_value=83, step=1)
    income=st.number_input("Yearly Income (in$):", min_value=0, step=10000, format='%d')
    expenditure=st.number_input("Monthly Card Expenditure in($):", min_value=0, step=100, format='%d')
    house_owner=st.selectbox('Do you own a House:',options=[(1,'Yes'),(0,'No')], format_func=lambda x: x[1])[0]
    self_emp=st.selectbox('Are you Self Employed:',options=[(1,'Yes'),(0,'No')], format_func=lambda x: x[1])[0]
    dependents=st.number_input('Number of Dependents:', min_value=0, step=1, format='%d')
    curr_add=st.number_input('Months Lived in Current Address:', min_value=0, step=1, format='%d')    
    major_cards=st.number_input('Number of Major Credit Cards Held:', min_value=0, step=1, format='%d')
    active_accounts=st.number_input('Number of Active Credit Accounts', min_value=0, step=1, format='%d')

    submitted=st.form_submit_button('Submit')

# Ensure correct data types and print debug information
if submitted:
    st.write("Reports:", reports, type(reports))
    st.write("Age:", age, type(age))
    st.write("Income:", income, type(income))
    st.write("Expenses:", expenses, type(expenses))
    st.write("House Owner:", house_owner, type(house_owner))
    st.write("Self Employed:", self_employed, type(self_employed))
    st.write("Dependents:", dependents, type(dependents))
    st.write("Months Address:", months_address, type(months_address))
    st.write("Major Cards:", major_cards, type(major_cards))
    st.write("Credit Accounts:", credit_accounts, type(credit_accounts))

if submitted:
    feature_array=np.array
    (
        [
            [reports, age, income, expenditure, 
            int(house_owner), int(self_emp), dependents, 
            curr_add, major_cards, active_accounts]
        ]
    )

    prediction=model.predict(feature_array)[0]

    if prediction==1:
        result='Credit Card Approved'
    else:
        result='Credit Card Not Approved'

    st.subheader(result)

