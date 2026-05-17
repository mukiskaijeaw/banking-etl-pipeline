-- 1. ดู transaction ทั้งหมด แบ่งตาม ampunt_tier
SELECT
    amount_tier,
    COUNT(*) AS total_transactions,
    ROUND(AVG("Amount")::numeric, 2) AS avg_amount,
    ROUND(SUM("Amount")::numeric, 2) AS total_amount
FROM fact_transactions
GROUP BY amount_tier
ORDER BY total_amount DESC;

-- 2. Fraud vs Normal -- dataset นี้มี column "Class" (0=normal, 1=fraud)
SELECT
    "Class"
    COUNT(*) AS count,
    ROUND(AVG("Amount")::numeric, 2) AS avg_amount,
    ROUND(SUM("Amount")::numeric, 2) AS total_amount
FROM fact_transactions
GROUP BY "Class";

-- 3. Window function -- rank transactions by amount
SELECT
    "Time",
    "Amount",
    "Class",
    RANK() OVER (ORDER BY "Amount" DESC) AS amount_rank,
    ROUND(AVG("Amount") OVER (), 2) AS overall_avg
FROM fact_transactions
LIMIT 20;

-- 4. Running total ของ fraud transactions
SELECT
    "Time",
    "Amount",
    SUM("Amount") OVER (
        ORDER BY "Time"
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_fraud
FROM fact_transactions
WHERE "Class" = 1
ORDER BY "Time";
    