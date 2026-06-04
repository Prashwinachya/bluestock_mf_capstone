from pathlib import Path
import pandas as pd

RAW_PATH = Path("Data/raw")

for file in RAW_PATH.glob("*.csv"):

    print("\n" + "=" * 50)
    print("FILE:", file.name)

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())