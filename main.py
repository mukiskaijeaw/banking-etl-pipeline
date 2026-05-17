import logging
import sys
sys.path.append('src')

from extract import extract_transactions
from transform import transform
from load import load_transactions

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'

)

def run_pipeline(filepath: str):
    print("=" * 50)
    print("BANKING ETL PIPELINE STARTING")
    print("=" * 50)

    # Step 1: Extract
    raw_df = extract_transactions(filepath)

    # Step 2: Transform
    clean_df = transform(raw_df)

    # Step 3: Load
    load_transactions(clean_df, mode='replace')

    print("=" * 50)
    print(f"✓ PIPELINE COMPLETE!")
    print(f"✓ Total records loaded: {len(clean_df)}")
    print("=" * 50)

if __name__ == "__main__":
    run_pipeline('data/raw/creditcard.csv')