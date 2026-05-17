import pandas as pd
import logging

logger = logging.getLogger(__name__)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean null values and transform data types"""
    df = df.copy()

    #count null before cleaning
    null_count = df.isnull().sum().sum()
    logger.info(f"Found {null_count} null values")

    #deleate rows at Amount is null
    df = df.dropna(subset=['Amount'])

    #delete duplicate
    dupes = df.duplicated().sum()
    df = df.drop_duplicates()
    logger.info(f"Removed {dupes} duplicates")

    # Standardize Amount ให้ไม่ติดลบ
    df['Amount'] = df['Amount'].abs()

    return df
def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add columns"""
    df = df.copy()

    #แบ่ง Amount เป็น tier
    df['amount_tier'] = pd.cut(
        df['Amount'],
        bins=[0, 10, 100, 1000, float('inf')],
        labels=['small', 'medium', 'large', 'very_large']

    )

    # Flag anomaly (Amount สูงผิดปกติ)
    mean = df['Amount'].mean()
    std = df['Amount'].std()
    df['is_anomaly'] = (df['Amount'] - mean).abs() > 3 * std

    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Main Pipeline"""
    df = clean_data(df)
    df = add_features(df)
    logger.info(f"Transform complete: {len(df)} rows")
    return df

if __name__ == "__main__":
    from extract import extract_transactions
    df = extract_transactions('data/raw/creditcard.csv')
    df_clean = transform(df)
    print(df_clean.shape)
    print(df_clean[['Amount', 'amount_tier', 'is_anomaly']].head(10))