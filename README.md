# Banking Transaction ETL Pipeline

An end-to-end ETL pipeline for processing credit card transaction data, 
built with Python and PostgreSQL.

---

## Project Overview

This project simulates a real-world data engineering workflow used in 
banking — extracting raw transaction data, cleaning and transforming it, 
loading it into a structured database, and running SQL analysis to detect 
fraud patterns.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python (Pandas) | Data extraction & transformation |
| PostgreSQL | Data warehouse |
| SQLAlchemy | Database connection |
| SQL (Window Functions) | Data analysis |
| Git / GitHub | Version control |

---

## Pipeline Architecture

**Extract** — Read raw credit card transaction CSV (284,807 rows)  
**Transform** — Clean nulls, remove 1,081 duplicates, add derived columns  
**Load** — Store cleaned data into PostgreSQL database  
**Analyze** — Run SQL window function queries for fraud detection insights  

---

##  Key Results

- Processed **284,807** transaction records
- Removed **1,081** duplicate entries
- Detected transactions flagged as anomalies using 3-sigma rule
- Identified fraud vs normal transaction patterns using SQL aggregation

---

##  How to Run

**1. Clone the repository**
```bash
git clone https://github.com/mukiskaijeaw/banking-etl-pipeline.git
cd banking-etl-pipeline
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up PostgreSQL**
- Create a database named `banking_db`
- Update DB credentials in `src/load.py` if needed

**4. Add dataset**
- Download from [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Place `creditcard.csv` in `data/raw/`

**5. Run the pipeline**
```bash
python main.py
```

**6. Run SQL analysis**
- Open `sql/analysis_queries.sql` in pgAdmin
- Run queries against `banking_db`

---

##  Project Structure
---

##  Author

**Chomphunut Unmee**  
Aspiring Data Engineer | Bioscience & Technology Graduate  
[GitHub](https://github.com/mukiskaijeaw)