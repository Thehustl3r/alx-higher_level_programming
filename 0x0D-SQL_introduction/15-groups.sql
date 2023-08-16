-- sql command
-- sql cmd to get number of entty
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
