-- 1
SELECT *
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2
SELECT
AVG(nav)
FROM fact_nav;

-- 3
SELECT
state,
SUM(amount_inr)
FROM fact_transactions
GROUP BY state;

-- 4
SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5
SELECT
fund_house,
COUNT(*)
FROM dim_fund
GROUP BY fund_house;

-- 6
SELECT
risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

-- 7
SELECT
AVG(sharpe_ratio)
FROM fact_performance;

-- 8
SELECT
MAX(return_5yr_pct)
FROM fact_performance;

-- 9
SELECT
MIN(max_drawdown_pct)
FROM fact_performance;

-- 10
SELECT
category,
COUNT(*)
FROM dim_fund
GROUP BY category;