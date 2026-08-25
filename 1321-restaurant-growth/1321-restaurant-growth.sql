# Write your MySQL query statement below
SELECT 
    t1.visited_on AS visited_on,
    SUM(t2.amount) AS amount,
    ROUND(SUM(t2.amount) / 7, 2) AS average_amount
FROM (SELECT DISTINCT visited_on 
        FROM Customer) t1
JOIN Customer t2 
ON t2.visited_on BETWEEN DATE_SUB(t1.visited_on, INTERVAL 6 DAY) AND t1.visited_on
GROUP BY t1.visited_on
HAVING COUNT(DISTINCT t2.visited_on) = 7
ORDER BY t1.visited_on