from pathlib import Path

import pandas as pd
import streamlit as st
import plotly.express as px

# Page setup
st.set_page_config(
    page_title="Nassau Candy | Profitability Dashboard",
    page_icon="🍫",
    layout="wide"
)

# Load dataset
PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "Nassau Candy Distributor.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)

    for col in ["Sales", "Cost", "Gross Profit", "Units"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


try:
    df = load_data()
except FileNotFoundError:
    st.error(f"Dataset not found: {DATA_PATH}")
    st.stop()

# Header
st.title("🍫 Nassau Candy Distributor")
st.subheader("Product Line Profitability & Margin Performance")
st.caption(
    "Interactive analysis of sales, costs, gross profit, "
    "product performance, and division contribution."
)

# Sidebar filters
st.sidebar.header("Dashboard Filters")

divisions = sorted(df["Division"].dropna().unique().tolist())
selected_divisions = st.sidebar.multiselect(
    "Select divisions",
    divisions,
    default=divisions
)

available_products = sorted(
    df.loc[df["Division"].isin(selected_divisions), "Product Name"]
    .dropna()
    .unique()
    .tolist()
)

selected_products = st.sidebar.multiselect(
    "Select products",
    available_products,
    default=available_products
)

filtered_df = df[
    df["Division"].isin(selected_divisions)
    & df["Product Name"].isin(selected_products)
].copy()

if filtered_df.empty:
    st.warning("No data matches the selected filters.")
    st.stop()

# KPIs
sales = filtered_df["Sales"].sum()
cost = filtered_df["Cost"].sum()
profit = filtered_df["Gross Profit"].sum()
units = filtered_df["Units"].sum()
margin = profit / sales * 100 if sales else 0

st.header("Key Performance Indicators")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Sales", f"${sales:,.2f}")
c2.metric("Total Cost", f"${cost:,.2f}")
c3.metric("Gross Profit", f"${profit:,.2f}")
c4.metric("Gross Margin", f"{margin:.2f}%")

st.metric("Total Units Sold", f"{units:,.0f}")
st.divider()

# Product summary
st.header("Product Profitability Analysis")
test_fig = px.bar(
    x=["Product A", "Product B", "Product C"],
    y=[1200, 950, 700],
    title="Plotly Rendering Test"
)

st.plotly_chart(test_fig, use_container_width=True)


product_summary = (
    filtered_df.groupby("Product Name", as_index=False)
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

left, right = st.columns(2)


with left:
    sales_chart = product_summary.sort_values("Sales")

    fig = px.bar(
        sales_chart,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Sales by Product",
        labels={
            "Sales": "Sales ($)",
            "Product Name": "Product"
        }
    )

    st.write("Chart data points:", len(fig.data))
    st.write("Products in chart:", len(sales_chart))

    st.plotly_chart(fig, use_container_width=True)


with right:
    profit_chart = product_summary.sort_values("Gross_Profit")
    fig = px.bar(
        profit_chart,
        x="Gross_Profit",
        y="Product Name",
        orientation="h",
        title="Gross Profit by Product",
        labels={
            "Gross_Profit": "Gross Profit ($)",
            "Product Name": "Product"
        }
    )
    st.plotly_chart(fig, use_container_width=True)

# Margin threshold
st.divider()
st.header("Gross Margin Performance")

margin_threshold = st.slider(
    "Minimum gross margin (%)",
    min_value=0,
    max_value=100,
    value=50,
    step=5
)

margin_results = product_summary[
    product_summary["Gross_Margin_%"] >= margin_threshold
].sort_values("Gross_Margin_%", ascending=False)

st.write(f"Products meeting this margin threshold: {len(margin_results)}")

st.dataframe(
    margin_results,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Sales": st.column_config.NumberColumn("Sales", format="$%.2f"),
        "Cost": st.column_config.NumberColumn("Cost", format="$%.2f"),
        "Gross_Profit": st.column_config.NumberColumn(
            "Gross Profit", format="$%.2f"
        ),
        "Gross_Margin_%": st.column_config.NumberColumn(
            "Gross Margin", format="%.2f%%"
        ),
        "Profit_Per_Unit": st.column_config.NumberColumn(
            "Profit per Unit", format="$%.2f"
        )
    }
)

# Division analysis
st.divider()
st.header("Division Performance")

division_summary = (
    filtered_df.groupby("Division", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Gross_Profit=("Gross Profit", "sum"),
        Units=("Units", "sum")
    )
)

division_summary["Gross_Margin_%"] = (
    division_summary["Gross_Profit"]
    / division_summary["Sales"].replace(0, float("nan"))
    * 100
)

d1, d2 = st.columns(2)

with d1:
    fig = px.pie(
        division_summary,
        names="Division",
        values="Sales",
        title="Sales Contribution by Division",
        hole=0.4
    )
    st.plotly_chart(fig, use_container_width=True)

with d2:
    fig = px.bar(
        division_summary,
        x="Division",
        y="Gross_Profit",
        color="Division",
        title="Gross Profit by Division",
        labels={"Gross_Profit": "Gross Profit ($)"}
    )
    st.plotly_chart(fig, use_container_width=True)

st.dataframe(division_summary, use_container_width=True, hide_index=True)

# Pareto analysis
st.divider()
st.header("Product Sales Concentration")

pareto = product_summary.sort_values("Sales", ascending=False).copy()

if pareto["Sales"].sum() > 0:
    pareto["Cumulative_Sales_%"] = (
        pareto["Sales"].cumsum() / pareto["Sales"].sum() * 100
    )

    fig = px.line(
        pareto,
        x="Product Name",
        y="Cumulative_Sales_%",
        markers=True,
        title="Cumulative Share of Sales by Product"
    )
    fig.update_yaxes(title="Cumulative Sales (%)", range=[0, 105])
    fig.update_xaxes(tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

# Raw data
with st.expander("View filtered dataset"):
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

# Data quality notice
st.divider()
st.warning(
    "Data quality notice: the supplied shipping dates appear inconsistent "
    "with order dates. Shipping performance is excluded from this dashboard. "
    "The original dates have not been artificially corrected."
)

st.caption("Nassau Candy Distributor | Product Line Profitability Analysis")
