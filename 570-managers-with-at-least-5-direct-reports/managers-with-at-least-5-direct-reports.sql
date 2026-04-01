# Write your MySQL query statement below
SELECT e.name
FROM Employee e
Join (
    SELECT  managerID
    FROM Employee
    GROUP BY managerID
    HAVING count(*) >= 5
)m
on e.id = m.managerID