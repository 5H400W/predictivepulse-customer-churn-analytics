# 📊 PredictivePulse

![Python][(https://img.shields.io/badge/Python?logo=python](https://github.com/5H400W/predictivepulse-customer-churn-analytics/blob/main/snapshot/Top-Churn-Drivers-Screenshot.png)
![Pandas](https://img.shields.io/badge/Pandas-Dataring-blue?logo=pandas
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machinege?logo=scikitlearn
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-amlit
![Plotly](https://img.shields.io/badge/Plottive%20Charts-green?logo=plotly
![Random Forest](https://img.shields.io/badge/Modelsuccess
![ROC-AUC](https://img.shields.io/badge/ROC--AUC-0.822en

---

## 🚀 Live Demo

**Deployment Coming Soon**

```text
https://predictivepulse.streamlit.app
```

---

# 🎯 Project Overview

PredictivePulse is an end-to-end Customer Churn Analytics and Prediction Platform built using Python, Pandas, Scikit-Learn, Plotly, and Streamlit.

The solution follows a Medallion Architecture inspired approach consisting of:

```text
Raw Data
   ↓
Bronze Layer
   ↓
Silver Layer
   ↓
Gold Layer
   ↓
Feature Engineering
   ↓
Machine Learning
   ↓
Risk Scoring
   ↓
Executive Dashboard
```

The project demonstrates real-world skills in:

- Data Engineering
- ETL Development
- Exploratory Data Analysis
- Customer Analytics
- Machine Learning
- Model Evaluation
- Business Intelligence
- Dashboard Development

---

# 🏗️ Architecture

```text
Raw Customer Dataset
        │
        ▼
Bronze Layer
(Data Ingestion)
        │
        ▼
Silver Layer
(Data Cleansing)
        │
        ▼
Gold Layer
(Feature Engineering)
        │
        ▼
Exploratory Analysis
        │
        ▼
Random Forest Model
        │
        ▼
Customer Risk Scoring
        │
        ▼
Interactive Dashboard
```

---

# 📊 Project Achievements

## Data Engineering

✅ Implemented Medallion Architecture

```text
Bronze
↓
Silver
↓
Gold
```

✅ Automated ETL Pipeline

✅ Data Quality Validation

✅ Feature Engineering Pipeline

---

## Analytics

✅ Churn Trend Analysis

✅ Contract Analysis

✅ Internet Service Analysis

✅ Payment Method Analysis

✅ Customer Tenure Analysis

✅ Revenue Behavior Analysis

---

## Machine Learning

✅ Random Forest Classification

✅ Feature Importance Analysis

✅ ROC-AUC Model Evaluation

✅ Threshold Optimization

✅ Customer Risk Scoring Engine

---

# 📈 Business Results

| Metric | Value |
|----------|----------|
| Total Customers Analyzed | 7,043 |
| Churn Rate | 26.54% |
| Model Accuracy | 76.58% |
| ROC-AUC Score | 0.8225 |
| Recommended Threshold | 0.40 |
| Recall @ Threshold 0.40 | 74.87% |
| High Risk Customers Identified | 1,724 |

---

# 📸 Dashboard Preview

## Executive Dashboard

The dashboard provides business users with customer churn insights, machine learning predictions, and retention opportunities.

![Executiveustomer-risk-explorer.png

---

## Churn Rate by Contract

Month-to-Month customers show significantly higher churn rates compared to annual contract customers.

snapshots/churn-rate-by-contract.png

---

## Churn Rate by Internet Service

Fiber Optic customers have the highest churn behavior within the customer base.

snapshots/churn-rate-by-internet-service.png

---

## Churn Rate by Payment Method

Electronic Check customers display significantly higher churn rates than customers using automated payment methods.

snapshots/churn-rate-by-payment-method.png

---

## Customer Tenure Distribution

Long-term customers show lower churn tendencies compared to newly acquired customers.

snapshots/customer-tenure-distribution.png

---

## Monthly Charges vs Churn

Higher monthly charges are associated with an increased likelihood of customer churn.

snapshots/monthly-charges-vs-churn.png

---

## Feature Importance Analysis

The Random Forest model identifies the strongest churn drivers.

snapshots/feature-importance.png

---

## Top Churn Drivers

The following variables contribute most strongly to churn prediction:

- Total Charges
- Customer Lifetime Value
- Monthly Charges
- Tenure
- Contract Type
- Online Security
- Tech Support
- Electronic Check Payment Method

![Top Churn Drivers-drivers.png

---

# 🤖 Model Performance

## ROC Curve

The ROC Curve evaluates how effectively the model separates churned customers from retained customers.

### ROC-AUC Score

```text
0.8225
```

An ROC-AUC above 0.80 indicates strong predictive capability.

snapshots/roc-curve.png

---

## Threshold Optimization

Threshold tuning was performed to determine the optimal balance between Precision and Recall.

### Recommended Threshold

```text
0.40
```

### Performance at 0.40

```text
Precision : 51.19%
Recall    : 74.87%
```

This threshold maximizes churn detection while keeping false positives within an acceptable range.

snapshots/precision-vs-recall.png

---

# 🔍 Customer Risk Explorer

The solution generates customer-level churn scores.

Features include:

- Churn Probability
- Predicted Churn Status
- Risk Category
- Contract Information
- Monthly Charges
- Customer Tenure

This enables retention teams to proactively target high-risk customers.

snapshots/customer-risk-explorer.png

---

# 🧠 Key Business Insights

### Contract Type Matters

Customers with Month-to-Month contracts have substantially higher churn rates.

### Payment Behavior is Predictive

Electronic Check customers represent the highest-risk segment.

### Customer Lifetime Value Matters

Higher-value customers require proactive retention efforts because of their revenue impact.

### Customer Tenure Reduces Churn

Long-term customers are significantly more loyal than new customers.

---

# 💻 Technology Stack

## Data Engineering

- Python
- Pandas
- NumPy

## Machine Learning

- Scikit-Learn
- Random Forest

## Visualization

- Plotly
- Matplotlib
- Streamlit

## Model Persistence

- Joblib

## Version Control

- Git
- GitHub

---

# ▶️ How to Run

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/PredictivePulse.git
```

## Create Environment

```bash
python -m venv venv
```

## Activate Environment

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Full Pipeline

```bash
python src/ingestion.py

python src/cleaning.py

python src/feature_engineering.py

python src/eda.py

python src/train_model.py

python src/predict.py
```

## Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 🔮 Future Enhancements

- XGBoost Implementation
- MLflow Integration
- Explainable AI (SHAP)
- Azure Databricks Migration
- PySpark Processing
- Revenue At Risk Forecasting
- Real-Time Prediction API
- Customer Retention Recommendation Engine

---

# 👨‍💻 Author

**Prashant Dwivedi**

** Machine Learning | LLM | GEN AI | RAG | Data Architect | Data Analytics | Data Engineering |**

GitHub: https://github.com/YOUR_USERNAME](https://github.com/5H400W)

LinkedIn: https://linkedin.com/in/YOUR_PROFILE](https://www.linkedin.com/in/prashant-dwivedi-5532b3190/)

---

⭐ If you found this project useful, consider giving it a star.
