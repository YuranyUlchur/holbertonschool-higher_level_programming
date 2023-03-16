-- Number of shows by genre
-- GROUP BY clause to group the results by genre
-- HAVING clause is used to filter out genres
SELECT tv_show_genres.genre_id AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY number_of_shows DESC;
