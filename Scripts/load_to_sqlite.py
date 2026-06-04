from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path

engine = create_engine(
    "sqlite:///Data/DB/Bluestock_mf.db"
)

raw = Path("Data/raw")
processed = Path("Data/Processed")

# fund master
pd.read_csv(
    raw / "01_fund_master.csv"
).to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

# nav
pd.read_csv(
    processed / "clean_nav_history.csv"
).to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

# performance
pd.read_csv(
    processed / "clean_performance.csv"
).to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

# transactions
pd.read_csv(
    processed / "clean_transactions.csv"
).to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded successfully")

