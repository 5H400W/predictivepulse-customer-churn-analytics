from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    roc_curve
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FILE = PROJECT_ROOT / "data" / "gold" / "customer_features.csv"

MODEL_FILE = PROJECT_ROOT / "models" / "churn_model.pkl"

FEATURE_IMPORTANCE_FILE = (
    PROJECT_ROOT / "data" / "gold" / "feature_importance.csv"
)

THRESHOLD_FILE = (
    PROJECT_ROOT / "data" / "gold" / "threshold_analysis.csv"
)

ROC_FILE = (
    PROJECT_ROOT / "data" / "gold" / "roc_curve.png"
)

METRICS_FILE = (
    PROJECT_ROOT / "data" / "gold" / "model_metrics.csv"
)


def train():

    print("=" * 50)
    print("PREDICTIVEPULSE - MODEL TRAINING")
    print("=" * 50)

    df = pd.read_csv(DATA_FILE)

    X = df.drop(
        columns=[
            "customerID",
            "Churn",
            "Target"
        ]
    )

    y = df["Target"]

    categorical_cols = X.select_dtypes(
        include=["object", "string"]
    ).columns.tolist()

    numeric_cols = X.select_dtypes(
        exclude=["object", "string"]
    ).columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_cols
            ),
            (
                "num",
                "passthrough",
                numeric_cols
            )
        ]
    )

    model = RandomForestClassifier(
        n_estimators=300,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    )

    pipeline = Pipeline([
        ("prep", preprocessor),
        ("model", model)
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    probabilities = (
        pipeline.predict_proba(X_test)[:, 1]
    )

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    auc_score = roc_auc_score(
        y_test,
        probabilities
    )

    print(f"\nAccuracy : {accuracy:.4f}")
    print(f"AUC Score: {auc_score:.4f}")

    print("\nConfusion Matrix")
    print(confusion_matrix(
        y_test,
        predictions
    ))

    print("\nClassification Report")
    print(classification_report(
        y_test,
        predictions
    ))

    # --------------------------------------------------
    # FEATURE IMPORTANCE
    # --------------------------------------------------

    feature_names = (
        pipeline.named_steps["prep"]
        .get_feature_names_out()
    )

    importances = (
        pipeline.named_steps["model"]
        .feature_importances_
    )

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    })

    importance_df = (
        importance_df
        .sort_values(
            by="Importance",
            ascending=False
        )
    )

    print("\nTop 20 Features")

    print(
        importance_df.head(20)
    )

    importance_df.to_csv(
        FEATURE_IMPORTANCE_FILE,
        index=False
    )

    # --------------------------------------------------
    # ROC CURVE
    # --------------------------------------------------

    fpr, tpr, thresholds = roc_curve(
        y_test,
        probabilities
    )

    plt.figure(figsize=(8, 6))

    plt.plot(
        fpr,
        tpr,
        color="blue",
        linewidth=2,
        label=f"AUC = {auc_score:.3f}"
    )

    plt.plot(
        [0, 1],
        [0, 1],
        linestyle="--",
        color="gray"
    )

    plt.title("ROC Curve")

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        ROC_FILE,
        dpi=300
    )

    plt.close()

    # --------------------------------------------------
    # THRESHOLD ANALYSIS
    # --------------------------------------------------

    threshold_results = []

    for threshold in np.arange(
        0.20,
        0.81,
        0.05
    ):

        preds = (
            probabilities >= threshold
        ).astype(int)

        tn, fp, fn, tp = confusion_matrix(
            y_test,
            preds
        ).ravel()

        precision = (
            tp / (tp + fp)
            if (tp + fp) > 0
            else 0
        )

        recall = (
            tp / (tp + fn)
            if (tp + fn) > 0
            else 0
        )

        threshold_results.append([
            round(threshold, 2),
            round(precision, 4),
            round(recall, 4)
        ])

    threshold_df = pd.DataFrame(
        threshold_results,
        columns=[
            "Threshold",
            "Precision",
            "Recall"
        ]
    )

    print("\nThreshold Analysis")

    print(threshold_df)

    threshold_df.to_csv(
        THRESHOLD_FILE,
        index=False
    )

    # --------------------------------------------------
    # METRICS FILE
    # --------------------------------------------------

    metrics_df = pd.DataFrame({
        "Metric": [
            "Accuracy",
            "ROC_AUC"
        ],
        "Value": [
            accuracy,
            auc_score
        ]
    })

    metrics_df.to_csv(
        METRICS_FILE,
        index=False
    )

    joblib.dump(
        pipeline,
        MODEL_FILE
    )

    print("\nFiles Generated")

    print(MODEL_FILE)
    print(FEATURE_IMPORTANCE_FILE)
    print(THRESHOLD_FILE)
    print(ROC_FILE)
    print(METRICS_FILE)


if __name__ == "__main__":
    train()