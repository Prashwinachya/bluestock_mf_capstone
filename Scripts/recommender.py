import pandas as pd

df = pd.read_csv(
    "Data/raw/07_scheme_performance.csv"
)

def recommend_funds(
    risk_grade="Low"
):

    filtered = df[
        df["risk_grade"] == risk_grade
    ]

    result = filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    )

    return result[
        [
            "scheme_name",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ].head(5)

print(
    recommend_funds()
)