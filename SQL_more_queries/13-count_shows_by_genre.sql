-- Number of shows by genre
SELECT sh.title, sg.genre_id
FROM tv_shows AS sh 
LEFT JOIN tv_show_genres AS sg
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY sh.title, sg.genre_id ASC;
