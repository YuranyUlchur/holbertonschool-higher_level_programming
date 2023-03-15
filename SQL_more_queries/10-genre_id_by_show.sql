-- Cities by States
use hbtn_0d_tvshows;
SELECT sh.title, sg.genre_id
FROM tv_shows AS sh 
JOIN tv_show_genres AS sg
ON sh.id = sg.show_id
ORDER BY sh.title, sg.genre_id ASC;
