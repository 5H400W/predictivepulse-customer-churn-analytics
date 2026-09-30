from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="PredictivePulse",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RISK_FILE = (
    BASE_DIR /
    "data" /
    "gold" /
    "customer_risk_scores.csv"
)

FEATURE_FILE = (
    BASE_DIR /
    "data" /
    "gold" /
    "feature_importance.csv"
)

THRESHOLD_FILE = (
    BASE_DIR /
    "data" /
    "gold" /
    "threshold_analysis.csv"
)

METRICS_FILE = (
    BASE_DIR /
    "data" /
    "gold" /
    "model_metrics.csv"
)

ROC_FILE = (
    BASE_DIR /
    "data" /
    "gold" /
    "roc_curve.png"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv(RISK_FILE)

feature_df = pd.read_csv(FEATURE_FILE)

threshold_df = pd.read_csv(THRESHOLD_FILE)

metrics_df = pd.read_csv(METRICS_FILE)

accuracy = round(
    metrics_df.loc[
        metrics_df["Metric"] == "Accuracy",
        "Value"
    ].iloc[0] * 100,
    2
)

auc_score = round(
    metrics_df.loc[
        metrics_df["Metric"] == "ROC_AUC",
        "Value"
    ].iloc[0],
    4
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📊 PredictivePulse")
st.markdown(
    "### Customer Churn Analytics & Prediction Dashboard"
)

# --------------------------------------------------
# KPI SECTION
# --------------------------------------------------

total_customers = len(df)

churn_rate = round(
    df["Target"].mean() * 100,
    2
)

high_risk = len(
    df[df["RiskLevel"] == "High"]
)

avg_revenue = round(
    df["MonthlyCharges"].mean(),
    2
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Customers",
    f"{total_customers:,}"
)

col2.metric(
    "Churn %",
    churn_rate
)

col3.metric(
    "Model Accuracy %",
    accuracy
)

col4.metric(
    "AUC Score",
    auc_score
)

col5.metric(
    "High Risk",
    f"{high_risk:,}"
)

st.divider()

# --------------------------------------------------
# CONTRACT CHURN
# --------------------------------------------------

left, right = st.columns(2)

with left:

    contract = (
        df.groupby("Contract")["Target"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        contract,
        x="Contract",
        y="Target",
        title="Churn Rate by Contract",
        text_auto=".2%"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    internet = (
        df.groupby("InternetService")["Target"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        internet,
        x="InternetService",
        y="Target",
        title="Churn Rate by Internet Service",
        text_auto=".2%"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# PAYMENT METHOD
# --------------------------------------------------

payment = (
    df.groupby("PaymentMethod")["Target"]
    .mean()
    .reset_index()
)

fig = px.bar(
    payment,
    x="PaymentMethod",
    y="Target",
    title="Churn Rate by Payment Method",
    text_auto=".2%"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# TENURE AND CHARGES
# --------------------------------------------------

left, right = st.columns(2)

with left:

    fig = px.histogram(
        df,
        x="tenure",
        color="Churn",
        nbins=30,
        title="Customer Tenure Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.box(
        df,
        x="Churn",
        y="MonthlyCharges",
        color="Churn",
        title="Monthly Charges vs Churn"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# --------------------------------------------------
# FEATURE IMPORTANCE
# --------------------------------------------------

st.subheader("Top Churn Drivers")

top_features = feature_df.head(15)

fig = px.bar(
    top_features,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Feature Importance"
)

fig.update_layout(
    yaxis=dict(
        autorange="reversed"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# THRESHOLD ANALYSIS
# --------------------------------------------------

st.subheader("Threshold Analysis")

fig = px.line(
    threshold_df,
    x="Threshold",
    y=["Precision", "Recall"],
    markers=True,
    title="Precision vs Recall"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# ROC CURVE
# --------------------------------------------------

st.subheader("ROC Curve")

st.image(str(ROC_FILE))

# --------------------------------------------------
# CUSTOMER SEARCH
# --------------------------------------------------

st.subheader("Customer Risk Explorer")

customer = st.selectbox(
    "Select Customer",
    sorted(df["customerID"].unique())
)

result = (
    df[df["customerID"] == customer]
)

st.dataframe(
    result[
        [
            "customerID",
            "ChurnProbability",
            "RiskLevel",
            "Contract",
            "tenure",
            "MonthlyCharges"
        ]
    ]
)

# --------------------------------------------------
# HIGH RISK CUSTOMERS
# --------------------------------------------------

st.subheader("Top 100 High Risk Customers")

st.dataframe(
    df.sort_values(
        "ChurnProbability",
        ascending=False
    ).head(100)
)