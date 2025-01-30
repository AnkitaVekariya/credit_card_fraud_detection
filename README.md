# Credit Card Fraud Detection

## Overview
This project detects fraudulent credit card transactions using machine learning. The dataset is highly imbalanced, requiring resampling techniques like **SMOTE**. Models used include **Logistic Regression, Random Forest, and XGBoost**.

## Files
- **EDA.ipynb** - Exploratory Data Analysis (EDA)
- **model.ipynb** - Model training and evaluation

## Key Insights
- **Class Imbalance**: Fraud cases are rare.
- **Transaction Amount**: Fraudulent transactions tend to be smaller.
- **Feature Correlation**: Some PCA features strongly correlate with fraud.

## Preprocessing
- **Feature Scaling**: StandardScaler applied to `Time` and `Amount`.
- **Handling Imbalance**: **SMOTE** used to balance data.
- **Train-Test Split**: 70% training, 30% testing.

## Models & Performance
| Model | Precision | Recall | Accuracy | ROC-AUC |
|--------|------------|--------|------------|------------|
| Logistic Regression | 0.9744 | 0.9223 | 0.9489 | 0.9490 |
| Random Forest | 0.9998 | 1.0000 | 0.9999 | 0.9999 |
| XGBoost | 0.9995 | 1.0000 | 0.9997 | 0.9997 |

## Conclusion
- **SMOTE improves recall** for fraud detection.
- **Future Work**: Feature engineering, hyperparameter tuning, anomaly detection.

🔗 **Dataset**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)

