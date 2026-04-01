# Write your MySQL query statement below
SELECT
    p.project_id,
    ROUND(
        COALESCE(SUM(e.experience_years) / COUNT(*), 0), 2
    ) average_years
FROM Project p
LEFT JOIN Employee e
ON p.employee_id = e.employee_id
GROUP BY project_id