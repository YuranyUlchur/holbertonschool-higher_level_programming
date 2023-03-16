-- List shows and genres
SELECT st.title, g.name
FROM tv_shows AS st
LEFT JOIN tv_show_genres AS sh
ON st.id = sh.show_id
LEFT JOIN tv_genres AS g
ON g.id = sh.genre_id
ORDER BY st.title, g.name ASC;
