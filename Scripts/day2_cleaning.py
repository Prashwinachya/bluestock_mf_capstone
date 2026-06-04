from pathlib import Path
import pandas as pd

RAW = Path("Data/raw")
PROCESSED = Path("Data/Processed")

PROCESSED.mkdir(exist_ok=True)

# --------------------------
# NAV HISTORY
# --------------------------

nav = pd.read_csv(RAW / "02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    PROCESSED / "clean_nav_history.csv",
    index=False
)

print("NAV cleaned")


# --------------------------
# INVESTOR TRANSACTIONS
# --------------------------

txn = pd.read_csv(
    RAW / "08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

txn = txn[txn["amount_inr"] > 0]

txn.to_csv(
    PROCESSED / "clean_transactions.csv",
    index=False
)

print("Transactions cleaned")


# --------------------------
# SCHEME PERFORMANCE
# --------------------------

perf = pd.read_csv(
    RAW / "07_scheme_performance.csv"
)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "expense_ratio_pct"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf = perf[
    perf["expense_ratio_pct"]
    .between(0.1, 2.5)
]

perf.to_csv(
    PROCESSED / "clean_performance.csv",
    index=False
)

print("Performance cleaned")