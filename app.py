import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

st.title("Credit Card Fraud Detection")

df = None
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

if df is not None:
    scaler = StandardScaler()
    df['Time_Scaled'] = scaler.fit_transform(df['Time'].values.reshape(-1, 1))
    df['Amount_Scaled'] = scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
    df.drop(['Time', 'Amount'], axis=1, inplace=True)
    
    X = df.drop(['Class'], axis=1)
    y = df['Class']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, 'fraud_model.pkl')  
    
    st.write("### Model Trained Successfully!")
    
    st.write("## Predict Fraudulent Transactions")
    st.write("Enter transaction details below:")
    
    user_input = {}
    for feature in X.columns:
        user_input[feature] = st.number_input(f"{feature}", value=0.0)
    
    if st.button("Predict Fraud Status"):
        model = joblib.load('fraud_model.pkl')
        input_df = pd.DataFrame([user_input])
        prediction = model.predict(input_df)[0]
        st.write(f"### Prediction: {'Fraud' if prediction == 1 else 'Not Fraud'}")
