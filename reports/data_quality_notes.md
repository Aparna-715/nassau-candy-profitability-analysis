# Data Quality Assessment — Nassau Candy Distributor

## Dataset overview

- Records: 10,194
- Columns: 18
- Missing values: 0 detected in the initial inspection
- Exact duplicate rows: 0 detected
- Product-profit validation: 0 inconsistent rows detected for Gross Profit = Sales - Cost

## Date validation findings

- Order date range: January 2, 2024 – December 31, 2025
- Shipping date range: June 30, 2026 – June 28, 2030
- Invalid dates detected during parsing: 0
- Negative shipping durations: 0
- Shipping durations over 30 days: 10,194
- Median shipping duration: 1,274 days

## Assessment

The shipping dates are inconsistent with ordinary shipping expectations. Even records labelled "Same Day" have shipping dates years after their order dates.

The cause has not been established. The original CSV must be preserved, and shipping dates must not be artificially corrected without evidence from the dataset source.

## Analysis limitations

Sales, cost, gross profit, units, product profitability and division performance can be analysed using the available fields, subject to the stated validations.

Shipping duration and delivery-performance conclusions are excluded pending investigation. Monthly sales trends should be treated cautiously until the order dates are verified against the original source documentation.
