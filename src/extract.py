import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_transactions(filepath: str) -> pd.DataFrame:
    """reads a CSV file and checks for file are loadable"""
    logger.info(f"Extracting data from {filepath}")

    df = pd.read_csv(filepath)

    logger.info(f"Extracted {len(df)} rows, {len(df.columns)} columns")
    return df

if __name__ == "__main__":
    df = extract_transactions('data/raw/creditcard.csv')
    print(df.shape)
    print(df.head())