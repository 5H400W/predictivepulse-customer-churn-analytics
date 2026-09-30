from pathlib import Path

import joblib
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_FILE = PROJECT_ROOT / "models" / "churn_model.pkl"

DATA_FILE = (
    PROJECT_ROOT /
    "data" /
    "gold" /
    "customer_features.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT /
    "data" /
    "gold" /
    "customer_risk_scores.csv"
)

THRESHOLD = 0.40


def predict():

    print("=" * 50)
    print("PREDICTIVEPULSE - SCORING")
    print("=" * 50)

    model = joblib.load(MODEL_FILE)

    df = pd.read_csv(DATA_FILE)

    X = df.drop(
        columns=[
            "customerID",
            "Churn",
            "Target"
        ]
    )

    probabilities = (
        model.predict_proba(X)[:, 1]
    )

    predictions = (
        probabilities >= THRESHOLD
    ).astype(int)

    df["ChurnProbability"] = (
        probabilities * 100
    ).round(2)

    df["PredictedChurn"] = predictions

    def risk_level(prob):

        if prob >= 70:
            return "High"

        elif prob >= 40:
            return "Medium"

        return "Low"

    df["RiskLevel"] = (
        df["ChurnProbability"]
        .apply(risk_level)
    )

    df.sort_values(
        by="ChurnProbability",
        ascending=False,
        inplace=True
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\nTop 10 Highest Risk Customers\n")

    print(
        df[
            [
                "customerID",
                "ChurnProbability",
                "RiskLevel"
            ]
        ].head(10)
    )

    print("\nOutput File")

    print(OUTPUT_FILE)

    print(
        f"\nHigh Risk Customers : "
        f"{len(df[df['RiskLevel']=='High'])}"
    )


if __name__ == "__main__":
    predict()