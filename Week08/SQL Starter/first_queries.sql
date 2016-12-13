SELECT address
FROM studio
WHERE name="MGM";

INSERT INTO moviestar
VALUES ("Sandra Bullock", "Y path", "F", "1969-07-06");

SELECT birthdate
FROM moviestar
WHERE name="Sandra Bullock";

SELECT name
FROM movieexec
WHERE networth > 10000;

SELECT name
FROM moviestar
WHERE gender="M" OR address="Prefect Rd";

INSERT INTO moviestar
VALUES ("Zahary Baharov", "Student City", "M", "1989-07-06");

DELETE FROM studio
WHERE address LIKE "%5%";

UPDATE studio
SET name="FOX"
WHERE name LIKE "%star%";

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
