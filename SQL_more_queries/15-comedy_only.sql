-- Only Comedy
SELECT st.name
FROM tv_shows AS st
JOIN tv_show_genres AS sh
ON st.id = sh.show_id
JOIN tv_genres AS g
ON g.id = sh.genre_id
WHERE g.name = "Comedy"
ORDER BY st.title ASC;
