-- Number of shows by genre
-- GROUP BY clause to group the results by genre
-- HAVING clause is used to filter out genres
SELECT gen.name AS genre, COUNT(gen.id) AS number_of_shows
FROM tv_genres AS gen
JOIN tv_show_genres AS sh
ON gen.id = sh.genre_id
GROUP BY gen.id
ORDER BY number_of_shows DESC;
