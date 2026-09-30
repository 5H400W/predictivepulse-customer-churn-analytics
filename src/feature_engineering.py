from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SILVER_FILE = PROJECT_ROOT / "data" / "silver" / "customer_clean.csv"
GOLD_FILE = PROJECT_ROOT / "data" / "gold" / "customer_features.csv"


def create_features():

    print("=" * 50)
    print("PREDICTIVEPULSE - GOLD LAYER")
    print("=" * 50)

    df = pd.read_csv(SILVER_FILE)

    # Customer Lifetime Value
    df["CustomerLifetimeValue"] = (
        df["tenure"] * df["MonthlyCharges"]
    )

    # High Value Customer
    df["HighValueCustomer"] = (
        df["MonthlyCharges"] > 80
    ).astype(int)

    # Long Term Customer
    df["LongTermCustomer"] = (
        df["tenure"] >= 24
    ).astype(int)

    # Count active services
    service_columns = [
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    df["ServiceCount"] = (
        df[service_columns]
        .eq("Yes")
        .sum(axis=1)
    )

    # Churn Target
    df["Target"] = (
        df["Churn"] == "Yes"
    ).astype(int)

    df.to_csv(
        GOLD_FILE,
        index=False
    )

    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print(f"Gold dataset saved to:")
    print(GOLD_FILE)

    print("\nNew Features Created:")
    print("- CustomerLifetimeValue")
    print("- HighValueCustomer")
    print("- LongTermCustomer")
    print("- ServiceCount")
    print("- Target")


if __name__ == "__main__":
    create_features()