
@'
# Nassau Candy Distributor
## Product Line Profitability & Margin Performance Analysis

## 1. Introduction

This project analyzes product-level sales and profitability for Nassau Candy Distributor. It uses exploratory data analysis and an interactive Streamlit dashboard to summarize revenue, costs, gross profit, gross margins, and division-level performance.

## 2. Problem Statement

Businesses need to understand which products contribute most to sales and gross profit, how profitability differs between products, and which divisions contribute most to revenue. This project organizes the supplied sales data into a set of descriptive metrics and visual analyses to support those decisions.

## 3. Project Objectives

- Analyze total sales, costs, gross profit, and units sold.
- Compare performance across business divisions.
- Identify products with high sales and high gross profit.
- Calculate product-level gross margins and profit per unit.
- Present the results in an interactive dashboard.
- Document data-quality issues that limit reliable interpretation.

## 4. Dataset Description

The dataset contains 10,194 rows and 18 columns in its original inspection.

Important fields include:
- Order ID and Row ID
- Order Date and Ship Date
- Customer ID
- Division and Region
- Product ID and Product Name
- Sales, Units, Gross Profit, and Cost

The inspected dataset contains 15 unique products, 5,044 unique customers, and 8,549 unique orders.

## 5. Tools and Technologies

- Python: analysis and data processing
- Pandas and NumPy: data manipulation and numerical calculations
- Matplotlib and Seaborn: exploratory visualizations
- Plotly: interactive charts
- Streamlit: interactive dashboard
- Visual Studio Code: development environment
- Git and GitHub: source control and project hosting

## 6. Methodology

### 6.1 Data Inspection

The dataset was inspected for its dimensions, column names, missing values, duplicate records, and data types.

### 6.2 Data Preparation

Numeric business measures were reviewed and converted to appropriate numeric types where required. Date fields were inspected separately because the supplied shipping dates showed inconsistencies.

### 6.3 Exploratory Data Analysis

The analysis examined:
- Sales by product
- Gross profit by product
- Sales by division
- Monthly sales trends
- Product gross margins
- Profit per unit
- Cumulative product sales concentration

### 6.4 Business Metrics

Gross margin was calculated as:

Gross Margin (%) = Gross Profit / Sales × 100

Profit per unit was calculated as:

Profit per Unit = Gross Profit / Units

The overall gross margin was calculated using total gross profit divided by total sales.

### 6.5 Dashboard Development

A Streamlit dashboard was developed to display key performance indicators and provide division and product filters. The dashboard includes product profitability, margin performance, division comparisons, sales concentration, and a filtered dataset view.

## 7. Results and Findings

### 7.1 Overall Performance

| Metric | Result |
|---|---:|
| Total Sales | $141,783.63 |
| Total Cost | $48,340.83 |
| Total Gross Profit | $93,442.80 |
| Overall Gross Margin | 65.91% |
| Total Units Sold | 38,654 |

### 7.2 Division Analysis

| Division | Sales |
|---|---:|
| Chocolate | $131,692.90 |
| Other | $9,663.25 |
| Sugar | $427.48 |

The Chocolate division contributes the largest share of sales in the inspected dataset.

### 7.3 Product Analysis

The highest-sales product was Wonka Bar - Triple Dazzle Caramel, with sales of $28,485.00.

The highest-gross-profit product was Wonka Bar -Scrumdiddlyumptious, with gross profit of $19,357.50.

Wonka Bar - Nutty Crunch Surprise recorded a gross margin of approximately 71.35%. Everlasting Gobstopper recorded an approximately 80% margin on sales of $130.00, illustrating that a high margin percentage does not necessarily imply a large financial contribution.

## 8. Data Quality and Limitations

The original inspection reported no missing values across the six key fields checked in the cleaned dataset and no exact duplicate rows in the earlier inspection.

A validation check found no inconsistencies greater than $0.01 between Gross Profit and Sales minus Cost.

However, the supplied shipping dates appear inconsistent with order dates. All inspected records showed shipping durations greater than 30 days, with a median of approximately 1,274 days. Even records marked Same Day showed implausibly long intervals.

The underlying cause has not been established. Therefore:
- Shipping-duration analysis has been excluded.
- The original dates have not been artificially corrected.
- Monthly sales trends should be interpreted cautiously until order dates are verified.
- Findings are descriptive and do not establish causal relationships.

## 9. Business Recommendations

1. Monitor sales, gross profit, and gross margin together when evaluating product performance.
2. Investigate leading products to understand their contribution to revenue and profitability.
3. Examine high-margin products with low sales to determine whether further investigation is justified.
4. Review the limited sales contribution of the Sugar division in the context of the business strategy.
5. Validate the source system's date fields before using shipping data for operational decisions.
6. Refresh the analysis periodically as reliable data becomes available.

These recommendations are proposed actions, not proven explanations of business performance.

## 10. Conclusion

The project demonstrates how Python-based analysis and an interactive Streamlit dashboard can summarize sales and profitability data for business stakeholders. The analysis identifies leading products, compares divisions, and highlights data-quality limitations that affect interpretation.

The results provide a foundation for further reporting and investigation. Reliable date data and additional business context would strengthen future operational and strategic analysis.

## 11. Project Structure

- `app.py`: Streamlit dashboard
- `data/`: source dataset and product summary
- `src/data_inspection.py`: data inspection
- `src/eda_analysis.py`: exploratory analysis and visualizations
- `src/date_diagnostics.py`: date-quality diagnostics
- `reports/executive_summary.md`: executive summary
- `reports/data_quality_notes.md`: data-quality documentation
- `reports/`: generated analysis charts

## 12. Future Improvements

- Resolve and document the source date inconsistencies.
- Improve dashboard chart rendering and test all interactive filters.
- Add automated data-validation checks.
- Add more business KPIs when supported by the available data.
- Publish a stable dashboard demo and update the project documentation.
'@ | Set-Content -Path "D:\project\reports\final_project_report.md" -Encoding utf8
