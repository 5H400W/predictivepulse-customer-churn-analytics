from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

GOLD_FILE = PROJECT_ROOT / "data" / "gold" / "customer_features.csv"


def run_eda():

    print("=" * 50)
    print("PREDICTIVEPULSE - EDA")
    print("=" * 50)

    df = pd.read_csv(GOLD_FILE)

    print(f"Dataset Shape: {df.shape}")

    churn_rate = df["Target"].mean() * 100

    print(f"\nChurn Rate: {churn_rate:.2f}%")

    print("\nCustomers By Churn")

    print(
        df["Churn"]
        .value_counts()
    )

    print("\nContract vs Churn")

    print(
        pd.crosstab(
            df["Contract"],
            df["Churn"],
            normalize="index"
        ) * 100
    )

    print("\nInternet Service vs Churn")

    print(
        pd.crosstab(
            df["InternetService"],
            df["Churn"],
            normalize="index"
        ) * 100
    )

    print("\nPayment Method vs Churn")

    print(
        pd.crosstab(
            df["PaymentMethod"],
            df["Churn"],
            normalize="index"
        ) * 100
    )

    print("\nAverage Monthly Charges")

    print(
        df.groupby("Churn")["MonthlyCharges"]
        .mean()
    )

    print("\nAverage Tenure")

    print(
        df.groupby("Churn")["tenure"]
        .mean()
    )


if __name__ == "__main__":
    run_eda()