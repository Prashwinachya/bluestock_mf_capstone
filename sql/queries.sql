-- Top 5 Funds by AUM

SELECT
scheme_name,
aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Top Fund Houses

SELECT
fund_house,
COUNT(*)
FROM dim_fund
GROUP BY fund_house;

-- Average Expense Ratio

SELECT
AVG(expense_ratio_pct)
FROM dim_fund;

-- High Sharpe Ratio Funds

SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC;

-- Lowest Drawdown Funds

SELECT
scheme_name,
max_drawdown_pct
FROM fact_performance
ORDER BY max_drawdown_pct DESC;