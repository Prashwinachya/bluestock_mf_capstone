import pandas as pd
import numpy as np

df = pd.read_csv("Data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(
    ["amfi_code", "date"]
)

df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
      .pct_change()
)

print(df.head())

df.to_csv(
    "Data/processed/daily_returns.csv",
    index=False
)

print("Daily returns calculated")