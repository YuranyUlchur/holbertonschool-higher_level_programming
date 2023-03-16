-- My genres
SELECT gen.name
FROM tv_genres AS gen
JOIN tv_show_genres AS sh
ON gen.id = sh.genre_id
WHERE a.show_id = (SELECT id FROM tv_shows WHERE title = "Dexter")
ORDER BY number_of_shows DESC;
