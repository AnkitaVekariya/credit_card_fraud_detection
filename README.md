# Credit Card Fraud Detection

## Overview
This project detects fraudulent credit card transactions using machine learning. The dataset is highly imbalanced, requiring resampling techniques like **SMOTE**. Models used include **Logistic Regression, Random Forest, and XGBoost**.

## Files
- **EDA.ipynb** - Exploratory Data Analysis (EDA)
- **model.ipynb** - Model training and evaluation
- **app.py** - Streamlit app for fraud detection

## How to Use
### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit App
```bash
streamlit run app.py
```

### 3. Use the App
- **Upload CSV**: Select a CSV file for batch fraud detection.
- **Manual Input**: Enter transaction details to check for fraud.
- **View Results**: Predictions and visualizations will be displayed.

## Dataset
🔗 [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
