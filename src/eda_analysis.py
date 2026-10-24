
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "Nassau Candy Distributor.csv"
OUTPUT_DIR = PROJECT_DIR / "reports"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH)

# Convert order dates
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%d-%m-%Y",
    errors="coerce"
)

# Create month column
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

sns.set_theme(style="whitegrid")

# 1. Sales by product
product_sales = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=True)
)

plt.figure(figsize=(11, 7))
product_sales.plot(kind="barh")
plt.title("Total Sales by Product")
plt.xlabel("Sales ($)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_by_product.png", dpi=300)
plt.close()

# 2. Gross profit by product
product_profit = (
    df.groupby("Product Name")["Gross Profit"]
    .sum()
    .sort_values(ascending=True)
)

plt.figure(figsize=(11, 7))
product_profit.plot(kind="barh")
plt.title("Gross Profit by Product")
plt.xlabel("Gross Profit ($)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "profit_by_product.png", dpi=300)
plt.close()

# 3. Sales by division
division_sales = df.groupby("Division")["Sales"].sum().sort_values()

plt.figure(figsize=(9, 5))
division_sales.plot(kind="bar")
plt.title("Sales by Division")
plt.xlabel("Division")
plt.ylabel("Sales ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_by_division.png", dpi=300)
plt.close()

# 4. Monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_sales_trend.png", dpi=300)
plt.close()

print("EDA completed successfully!")
print("Charts saved in:", OUTPUT_DIR)
print("\nTop 5 products by sales:")
print(product_sales.sort_values(ascending=False).head(5).round(2))

print("\nTop 5 products by gross profit:")
print(product_profit.sort_values(ascending=False).head(5).round(2))
