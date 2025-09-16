Telco Customer Churn Prediction
Project Overview

This project predicts which customers are likely to leave a telecom service, helping the company take proactive retention measures. The goal is to turn raw customer data into actionable insights using Machine Learning and an interactive web app.

Key Insights from EDA

Contract Type Matters: Customers with month-to-month contracts are far more likely to churn.

Tenure Impact: Longer-tenured customers are less likely to leave.

Monthly Charges Influence: Higher monthly bills correlate with higher churn probability.

Service Usage Patterns: Usage of internet-related services, security features, and streaming options influences customer retention.

These insights helped guide feature engineering and improved model accuracy.

Machine Learning Model

Algorithm: XGBoost Classifier

Performance: Achieved high accuracy and balanced F1-score on the test set.

Preprocessing: One-hot encoding for categorical features, alignment of training/testing columns.

Saved Model: churn_model.pkl for deployment in Streamlit.

Interactive Web App

Built with Streamlit, the app allows users to:

Enter customer information:

Tenure (Months)

Monthly Charges

Total Charges

Contract Type

Get real-time predictions:

Churn / No Churn

Probability of leaving

Try it yourself: Live Demo
