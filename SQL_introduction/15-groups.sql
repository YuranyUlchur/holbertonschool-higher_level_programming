-- Number by score
-- COUNT is used to count the number of rows in a table.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;;
