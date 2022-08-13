SELECT * FROM Tracks;
SELECT * FROM Artists;
SELECT * FROM top_artists;
SELECT * FROM top_tracks;




--Create Table for top_artists
SELECT name, 
	popularity,
	followers,
	popularity*followers AS total_popularity
INTO top_artists
FROM Artists
ORDER BY total_popularity DESC;

SELECT t.name,
	t.Artists,
	t.popularity,
	t.popularity*a.followers AS true_popularity
INTO top_tracks
FROM Tracks as t, Artists as a;

