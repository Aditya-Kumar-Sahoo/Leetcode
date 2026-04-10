# Write your MySQL query statement below
SELECT max(num) num
FROM(
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING count(num) = 1
)t