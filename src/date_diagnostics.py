
import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
file_path = project_dir / "data" / "Nassau Candy Distributor.csv"

df = pd.read_csv(file_path)

df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%d-%m-%Y", errors="coerce"
)
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="%d-%m-%Y", errors="coerce"
)

df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

print("First 10 rows:")
print(df[["Order Date", "Ship Date", "Shipping Days"]].head(10))

print("\nOrder date range:")
print(df["Order Date"].min(), "to", df["Order Date"].max())

print("\nShipping date range:")
print(df["Ship Date"].min(), "to", df["Ship Date"].max())

print("\nShipping duration statistics:")
print(df["Shipping Days"].describe())

print("\nMost common shipping dates:")
print(df["Ship Date"].value_counts().head(10))

print("\nRows with shipping duration over 30 days:")
print((df["Shipping Days"] > 30).sum(), "out of", len(df))

print("\n========== DATE SHIFT CHECK ==========")

# Compare the year and month of order and shipping dates
print("\nOrder dates by year:")
print(df["Order Date"].dt.year.value_counts().sort_index())

print("\nShipping dates by year:")
print(df["Ship Date"].dt.year.value_counts().sort_index())

# Show examples sorted by order date
print("\nEarliest orders:")
print(
    df.sort_values("Order Date")[
        ["Order ID", "Order Date", "Ship Date", "Ship Mode"]
    ].head(15).to_string(index=False)
)

print("\nLatest orders:")
print(
    df.sort_values("Order Date")[
        ["Order ID", "Order Date", "Ship Date", "Ship Mode"]
    ].tail(15).to_string(index=False)
)
