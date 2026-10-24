
@'
# Nassau Candy Distributor
## Executive Summary
### Product Line Profitability & Margin Performance Analysis

## 1. Project Overview

This project analyzes sales, costs, gross profit, units sold, and product-level profitability for Nassau Candy Distributor. The objective is to identify leading products, compare division performance, evaluate gross margins, and support data-driven business decisions.

## 2. Key Performance Indicators

| Metric | Result |
|---|---:|
| Total Sales | $141,783.63 |
| Total Cost | $48,340.83 |
| Total Gross Profit | $93,442.80 |
| Overall Gross Margin | 65.91% |
| Total Units Sold | 38,654 |
| Unique Products | 15 |
| Unique Customers | 5,044 |
| Unique Orders | 8,549 |

## 3. Key Findings

### Division Performance

The Chocolate division generated $131,692.90 in sales, making it the largest contributor to total sales. The Other division generated $9,663.25, while the Sugar division generated $427.48.

### Product Performance

Wonka Bar - Triple Dazzle Caramel recorded the highest sales at $28,485.00. Wonka Bar -Scrumdiddlyumptious generated the highest gross profit at $19,357.50.

Wonka Bar - Nutty Crunch Surprise achieved a gross margin of approximately 71.35%, while Everlasting Gobstopper achieved an approximately 80% gross margin on comparatively low sales of $130.00.

These findings illustrate why products should be evaluated using sales, gross profit, and margin together rather than relying on a single metric.

## 4. Business Recommendations

1. Review the leading products to understand their contribution to revenue and gross profit.
2. Investigate whether high-margin, low-sales products have opportunities for increased demand.
3. Monitor product-level gross margins alongside sales volume and gross profit.
4. Review the small contribution of the Sugar division to determine whether its current product mix meets business objectives.
5. Validate source-system date fields before using shipping data for operational performance analysis.

## 5. Data Quality and Limitations

The supplied shipping dates appear inconsistent with order dates. Shipping-duration analysis has therefore been excluded. The original dates have not been artificially corrected.

The findings in this summary are descriptive and do not establish the causes of product or division performance. Additional business context would be required before making operational or pricing decisions.

## 6. Conclusion

The analysis provides a consolidated view of sales, costs, gross profit, and product profitability. The results can help stakeholders identify important revenue contributors, compare product margins, and investigate opportunities for improvement. The dashboard and supporting analysis provide a foundation for further business reporting.

'@ | Set-Content -Path "D:\project\reports\executive_summary.md" -Encoding utf8
