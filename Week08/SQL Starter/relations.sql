SELECT starname
FROM starsin
WHERE movietitle="Terms of Endearment";

SELECT starname
FROM starsin, movie
WHERE movie.studioname="MGM" AND movie.title=starsin.movietitle AND movie.year = 1995;

ALTER TABLE studio ADD COLUMN president char(50);

UPDATE studio
SET president="Jackie Chan"
WHERE name="MGM";

UPDATE studio
SET president="Eddy Murphy"
WHERE name="USA Entertainm.";

SELECT president
FROM studio
WHERE name="MGM";

SELECT title
FROM movie
WHERE length > (SELECT length
					FROM movie
					WHERE title="Gone With the Wind");
					
SELECT name
FROM movieexec
WHERE networth > (SELECT networth
					FROM movieexec
					WHERE name="Merv Griffin");