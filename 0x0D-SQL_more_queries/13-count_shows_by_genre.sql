-- Count up shows by genre
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS 'number_shows' FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.`name` ORDER BY number_shows DESC;
