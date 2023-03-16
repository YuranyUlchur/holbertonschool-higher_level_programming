-- My genres
SELECT g.name
FROM tv_genres AS g
JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
JOIN tv_show AS sh
ON sh.id = sg.show_id
WHERE sh.title = "Dexter"
ORDER BY g.name;

