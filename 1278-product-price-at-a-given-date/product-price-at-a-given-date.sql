SELECT product_id,
       COALESCE(new_price, 10) AS price
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY product_id
               ORDER BY change_date DESC
           ) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
) t
WHERE rn = 1

UNION

SELECT product_id, 10
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16';