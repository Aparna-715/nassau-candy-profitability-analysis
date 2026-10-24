# 🍫 Nassau Candy Distributor
## Product Line Profitability & Margin Performance Analysis

An end-to-end data analytics project that examines product sales, costs, gross profit, and gross margins for Nassau Candy Distributor. The project includes exploratory data analysis, visual reports, and an interactive Streamlit dashboard.

## 🎯 Project Objectives

- Analyze sales and gross profit by product.
- Compare performance across business divisions.
- Identify products with strong gross margins.
- Examine sales and profitability patterns.
- Present key performance indicators through an interactive dashboard.
- Document data-quality issues and analytical limitations.

## 🛠️ Technologies Used

- **Python** — analysis and application logic
- **Pandas and NumPy** — data cleaning and calculations
- **Matplotlib and Seaborn** — exploratory visualizations
- **Plotly** — interactive charts
- **Streamlit** — dashboard application

## 📊 Key Results

| Metric | Result |
|---|---:|
| Total Sales | $141,783.63 |
| Total Cost | $48,340.83 |
| Gross Profit | $93,442.80 |
| Overall Gross Margin | 65.91% |
| Total Units Sold | 38,654 |
| Unique Products | 15 |

*These results are based on the supplied dataset and the analysis performed in this project.*

## 📁 Project Structure

```text
nassau-candy-profitability-analysis/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── Nassau Candy Distributor.csv
│   └── product_profitability_summary.csv
├── src/
│   ├── data_inspection.py
│   ├── date_diagnostics.py
│   └── eda_analysis.py
└── reports/
    ├── executive_summary.md
    ├── final_project_report.md
    ├── data_quality_notes.md
    ├── sales_by_product.png
    ├── profit_by_product.png
    ├── sales_by_division.png
    └── monthly_sales_trend.png
```

## 🚀 Run the Dashboard Locally

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Streamlit application:

   ```bash
   python -m streamlit run app.py
   ```

5. Open the local URL displayed in the terminal.

## 📈 Dashboard Features

- KPI cards for sales, cost, gross profit, gross margin, and units sold.
- Division and product filters.
- Product-level profitability comparisons.
- Gross-margin threshold analysis.
- Division performance visualizations.
- Product sales concentration analysis.
- Filtered dataset exploration.
- Data-quality notice.

## ⚠️ Data Quality and Limitations

The supplied shipping dates appear inconsistent with order dates. Shipping performance is therefore excluded from the dashboard, and the original dates have not been artificially corrected. Monthly trends should be interpreted cautiously until the source dates are verified.

Gross margin is calculated as gross profit divided by sales. The dashboard provides descriptive analytics and should not be interpreted as a forecast or a causal analysis.

## 📄 Reports

See the `reports/` directory for the executive summary, final project report, data-quality notes, and supporting charts.

## 👩‍💻 Project Status

The local Streamlit dashboard and analysis reports have been prepared. Deployment and final repository verification are the remaining steps.



