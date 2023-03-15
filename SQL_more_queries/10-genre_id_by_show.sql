-- Cities by States
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows AS tv_shows
JOIN tv_show_genres AS tv_show_genres 
ON tv_shows.id = tv_show_genres.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
