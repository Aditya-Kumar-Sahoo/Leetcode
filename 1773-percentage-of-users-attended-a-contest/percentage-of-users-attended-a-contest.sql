# Write your MySQL query statement below
SELECT 
    r.contest_id,
    (ROUND(COUNT(DISTINCT r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2)) percentage
FROM Users u
RIGHT JOIN Register r
ON u.user_id = r.user_id
GROUP BY r.contest_id
Order BY percentage DESC, r.contest_id