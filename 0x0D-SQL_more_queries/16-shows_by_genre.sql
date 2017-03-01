-- List all shows and their genres
SELECT tv_shows.title, tv_genres.name FROM tv_genres  RIGHT OUTER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id RIGHT OUTER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC;
