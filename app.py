import streamlit as st
import pandas as pd
import pickle

# ---- Load model ----
with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)

# ---- Page title ----
st.title("Telco Customer Churn Prediction")

# ---- Input section in columns ----
col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (Months)", min_value=0, help="عدد شهور العميل مع الشركة")
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, help="المصاريف الشهرية للعميل")

with col2:
    total_charges = st.number_input("Total Charges", min_value=0.0, help="إجمالي المصاريف للعميل")
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"], help="نوع العقد الحالي للعميل")

# ---- Prepare input data ----
data = {
    'tenure': [tenure],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges],
    'Contract': [contract]
}

input_df = pd.DataFrame(data)
input_df = pd.get_dummies(input_df)

# ---- Add missing columns from training ----
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0

# ---- Reorder columns ----
input_df = input_df[model.feature_names_in_]

# ---- Prediction ----
if st.button("Predict"):
    with st.spinner("Predicting..."):
        prediction = model.predict(input_df)[0]
        prediction_prob = model.predict_proba(input_df)[:,1][0]

        if prediction == 1:
            st.error(f"Prediction: Churn")
        else:
            st.success(f"Prediction: No Churn")
        
        st.info(f"Probability of leaving: {prediction_prob:.2f}")
