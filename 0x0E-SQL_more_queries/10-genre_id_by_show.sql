-- Import the database dump from hbtn_0d_tvshows
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
SELECT s.title, tv_show_genres.genre_id
FROM tv_shows AS s 
INNER JOIN tv_show_genres
ON s.id = tv_show_genres.show_id
ORDER BY s.title, tv_show_genres.genre_id;
