-- Number by score
-- COUNT is used to count the number of rows in a table.
SELECT score, COUNT(*) as count FROM second_table GROUP BY score;
