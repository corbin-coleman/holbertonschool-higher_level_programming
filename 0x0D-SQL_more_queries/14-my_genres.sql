-- List out all genres of a show
SELECT tv_genres.name FROM tv_genres JOIN tv_show_genres ON tv_show_genres.show_id = (SELECT tv_shows.id FROM tv_shows WHERE tv_shows.title = "Dexter") WHERE tv_show_genres.genre_id = tv_genres.id ORDER BY tv_genres.name ASC;
