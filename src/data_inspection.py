import numpy as np
import pandas as pd
from pathlib import Path

# Locate the project and dataset
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "Nassau Candy Distributor.csv"

# Load the dataset
df = pd.read_csv(DATA_PATH)

print("\n========== DATASET OVERVIEW ==========")
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== BUSINESS SUMMARY ==========")

# Check whether the expected columns exist
required = ["Sales", "Cost", "Gross Profit", "Units", "Division"]
missing_columns = [col for col in required if col not in df.columns]

if missing_columns:
    print("Please check these column names:", missing_columns)
else:
    print("Total Sales:", round(df["Sales"].sum(), 2))
    print("Total Cost:", round(df["Cost"].sum(), 2))
    print("Total Gross Profit:", round(df["Gross Profit"].sum(), 2))
    print("Total Units:", df["Units"].sum())

    total_sales = df["Sales"].sum()

    if total_sales != 0:
        margin = df["Gross Profit"].sum() / total_sales * 100
        print("Overall Gross Margin:", round(margin, 2), "%")

    print("\nSales by Division:")
    print(df.groupby("Division")["Sales"].sum().sort_values(ascending=False))

print("\n========== DATE INSPECTION ==========")

print("\nFirst 10 order and shipping dates:")
print(df[["Order Date", "Ship Date"]].head(10).to_string(index=False))

print("\nSample distinct date formats:")
print("Order Date examples:", df["Order Date"].drop_duplicates().head(5).tolist())
print("Ship Date examples:", df["Ship Date"].drop_duplicates().head(5).tolist())

print("\n========== PRODUCT INSPECTION ==========")
print("Unique products:", df["Product Name"].nunique())
print("Unique customers:", df["Customer ID"].nunique())
print("Unique orders:", df["Order ID"].nunique())

print("\nTop 10 products by sales:")
print(
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .round(2)
)
# coverting date format
df = pd.read_csv(DATA_PATH)

# Convert dates using the observed day-month-year format
df["Order Date"] = pd.to_datetime(
    df["Order Date"], format="%d-%m-%Y", errors="coerce"
)
df["Ship Date"] = pd.to_datetime(
    df["Ship Date"], format="%d-%m-%Y", errors="coerce"
)

print("========== DATE VALIDATION ==========")
print("Order date range:", df["Order Date"].min(), "to", df["Order Date"].max())
print("Ship date range:", df["Ship Date"].min(), "to", df["Ship Date"].max())

# Calculate shipping duration without changing the original data
df["Shipping Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

print("\nInvalid order dates:", df["Order Date"].isna().sum())
print("Invalid shipping dates:", df["Ship Date"].isna().sum())
print("Negative shipping durations:", (df["Shipping Days"] < 0).sum())
print("Shipping durations over 30 days:", (df["Shipping Days"] > 30).sum())
print("Median shipping duration:", df["Shipping Days"].median(), "days")

print("\n========== PROFIT VALIDATION ==========")

# Check whether Gross Profit = Sales - Cost
df["Calculated Profit"] = df["Sales"] - df["Cost"]
df["Profit Difference"] = (
    df["Gross Profit"] - df["Calculated Profit"]
).round(2)

print("Rows with inconsistent profit:",
      (df["Profit Difference"].abs() > 0.01).sum())

print("\n========== PRODUCT PROFITABILITY ==========")

product_summary = (
    df.groupby(["Product ID", "Product Name"], as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Cost=("Cost", "sum"),
        Gross_Profit=("Gross Profit", "sum"),
        Units=("Units", "sum")
    )
)

product_summary["Gross_Margin_%"] = (
    product_summary["Gross_Profit"]
    / product_summary["Sales"].replace(0, float("nan"))
    * 100
)

product_summary["Profit_Per_Unit"] = (
    product_summary["Gross_Profit"]
    / product_summary["Units"].replace(0, float("nan"))
)

product_summary = product_summary.sort_values(
    "Gross_Profit", ascending=False
)

print(product_summary.round(2).to_string(index=False))

# Save the product summary for later analysis
OUTPUT_PATH = PROJECT_DIR / "data" / "product_profitability_summary.csv"
product_summary.to_csv(OUTPUT_PATH, index=False)

print("\nProduct summary saved to:", OUTPUT_PATH)

# Investigate the date relationship without modifying the original data

print("\n========== DATE DIAGNOSTICS ==========")

print("\nFirst 10 parsed dates:")
print(df[["Order Date", "Ship Date"]].head(10).to_string(index=False))

print("\nMost common order dates:")
print(df["Order Date"].value_counts().head(10))

print("\nMost common shipping dates:")
print(df["Ship Date"].value_counts().head(10))

print("\nShipping duration distribution:")
shipping_days = (
    df["Ship Date"] - df["Order Date"]
).dt.days

print(shipping_days.describe())

print("\nFirst 10 rows with shipping duration:")
date_check = df[["Order Date", "Ship Date"]].copy()
date_check["Shipping Days"] = shipping_days
print(date_check.head(10).to_string(index=False))

