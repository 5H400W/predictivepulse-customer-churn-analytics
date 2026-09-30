from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

BRONZE_FILE = PROJECT_ROOT / "data" / "bronze" / "Telco_customer_churn.csv"
SILVER_FILE = PROJECT_ROOT / "data" / "silver" / "customer_clean.csv"


def clean_data():

    print("=" * 50)
    print("PREDICTIVEPULSE - SILVER LAYER")
    print("=" * 50)

    df = pd.read_csv(BRONZE_FILE)

    print(f"Original Rows : {len(df):,}")

    # Convert TotalCharges
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    removed = before - len(df)

    # Fill missing values
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    print(f"Duplicates Removed : {removed}")

    print("\nMissing Values")
    print(df.isnull().sum())

    SILVER_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        SILVER_FILE,
        index=False
    )

    print(f"\nSilver file saved to:")
    print(SILVER_FILE)


if __name__ == "__main__":
    clean_data()