SELECT m.title AS MOVIE, m.year, s.name AS "STUDIO NAME", s.address AS "STUDIO ADDRESS"
FROM movie AS m
JOIN studio AS s ON m.studioname=s.name
WHERE m.length > 120;

SELECT DISTINCT m.studioname, st.starname
FROM movie AS m
JOIN starsin AS st ON m.title=st.movietitle;

SELECT DISTINCT movieexec.name
FROM movieexec
JOIN movie  ON movieexec.cert=movie.producer
JOIN starsin AS st ON st.movietitle=movie.title
WHERE st.starname = "Harrison Ford";

SELECT star.name
FROM moviestar AS star
JOIN starsin AS st ON st.starname=star.name
JOIN movie ON movie.title=st.movietitle
WHERE star.gender='F' AND movie.studioname="MGM";

SELECT prod.name, m.title
FROM movieexec AS prod
JOIN movie AS m ON m.producer=prod.cert
WHERE m.producer=(SELECT producer
					FROM movie
					WHERE title="Star Wars");
						
INSERT INTO moviestar
VALUES ("Sandra Bullock", "Y path", 'F', "1969-07-06");

INSERT INTO moviestar
VALUES ("Zahary Baharov", "Student City", 'M', "1989-07-06");

SELECT star.name AS "Movie Star"
FROM moviestar AS star
LEFT JOIN starsin AS st ON star.name=st.starname
WHERE st.movietitle IS NULL;