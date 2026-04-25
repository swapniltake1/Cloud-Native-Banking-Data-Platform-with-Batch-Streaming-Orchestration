-- Partition by date for scalability
SELECT
    txn_id,
    account_id,
    amount,
    transaction_type,
    location,
    CASE
        WHEN amount > 100000 THEN 'HIGH'
        WHEN amount > 50000 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS amount_category,
    date(timestamp) AS transaction_date  -- For partitioning
FROM banking.banking.banking_bronze_transactions
WHERE txn_id IS NOT NULL