# 📊 Telco Customer Churn Prediction

This project focuses on predicting whether a customer will leave a telecom service. The dataset contains customer information, service details, and usage metrics. The analysis and model are designed to help the company reduce churn and improve customer retention.

---

## 🔍 Key Insights from EDA

### 1. Customer Tenure
- Customers with shorter tenure tend to churn more.
- Long-term customers are more loyal.

### 2. Contract Type
- Month-to-month contracts have the highest churn rate.
- One-year and Two-year contracts show lower churn rates.

### 3. Monthly & Total Charges
- Higher monthly charges slightly increase the churn probability.
- Total charges are lower for customers who recently joined, and these customers have higher churn risk.

### 4. Services Impact
- Customers with no online security, online backup, or tech support are more likely to churn.
- Streaming services usage does not strongly affect churn.

---

## 🧠 Machine Learning Model

- **Algorithm:** XGBoost Classifier  
- **Accuracy:** [Insert Accuracy Here]  
- **F1 Score:** [Insert F1 Score Here]  

The model predicts churn with good accuracy and handles categorical features using one-hot encoding.

---

## ⚡ How to Use

1. Enter customer details in the input fields:
    - Tenure (Months)  
    - Monthly Charges  
    - Total Charges  
    - Contract Type  
2. Click **Predict** to see:
    - Churn Prediction: Yes / No  
    - Probability of Leaving  

The interactive app is available here: [[Streamlit App Link](https://share.streamlit.io/your-app-link)](https://telcochurnapp-vnged85tccxv3vvjkvaqd3.streamlit.app)

---


