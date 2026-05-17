import pandas as pd 
from sqlalchemy import create_engine
import logging

logger = logging.getLogger(__name__)

DB_URL = "postgresql://postgres:postgres123@localhost:5432/banking_db"

def get_engine():
    return create_engine(DB_URL)

def load_transactions(df: pd.DataFrame, mode: str = 'replace'):
    engine = get_engine()

    df.to_sql(
        name= 'fact_transactions',
        con=engine,
        if_exists=mode,
        index=False,
        method='multi',
        chunksize=1000

    )
    logger.info(f"Loaded {len(df)} rows to fact_transactions")

if __name__ == "__main__":
    engine = get_engine()
    print("Connected to database!")
    print(engine)