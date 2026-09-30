from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_FILE = PROJECT_ROOT / "data" / "raw" / "Telco-Customer-Churn.csv"
BRONZE_FILE = PROJECT_ROOT / "data" / "bronze" / "Telco_customer_churn.csv"

def ingest_data():
    print("=" * 50)
    print("PREDICTIVEPULSE - INGESTION")
    print("=" * 50)

    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {RAW_FILE}"
        )

    df = pd.read_csv(RAW_FILE)

    print(f"Rows Loaded    : {len(df):,}")
    print(f"Columns Loaded : {len(df.columns)}")

    BRONZE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        BRONZE_FILE,
        index=False
    )

    print(f"Bronze file created: {BRONZE_FILE}")
    print("Ingestion complete.")


if __name__ == "__main__":
    ingest_data()