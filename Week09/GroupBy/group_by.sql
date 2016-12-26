SELECT AVG(speed)
FROM pc;

SELECT AVG(screen), product.maker
FROM product
INNER JOIN laptop ON product.model=laptop.model
GROUP BY product.maker;

SELECT AVG(speed)
FROM laptop
WHERE price > 1000;

SELECT AVG(price), hd
FROM pc
GROUP BY hd;


SELECT AVG(price)
FROM pc
GROUP BY speed
HAVING speed > 500;


SELECT AVG(price)
FROM product
INNER JOIN pc ON pc.model = product.model
GROUP BY product.maker
HAVING product.maker = 'A';

SELECT AVG(price)
FROM product
INNER JOIN pc ON pc.model = product.model
WHERE product.maker = 'A';

SELECT product.maker, (AVG(pc.price) + AVG(laptop.price)) / 2
FROM product
LEFT JOIN pc ON pc.model = product.model
LEFT JOIN laptop ON laptop.model = product.model
WHERE product.maker = 'B';

SELECT product.maker, COUNT(product.model)
FROM product
JOIN  pc ON product.model = pc.model
GROUP BY product.maker;
HAVING COUNT(product.model) > 3;

SELECT product.maker, MAX(pc.price)
FROM product
JOIN pc ON product.model = pc.model
WHERE pc.price = (SELECT MAX(price)
					FROM pc)
GROUP BY product.maker;


SELECT ls.maker, ls.Laptop_, ps.Printer_
FROM(SELECT COUNT(type) AS Laptop_, maker
		FROM product
		WHERE type="Laptop"
		GROUP BY maker) AS ls
LEFT JOIN (SELECT COUNT(type) AS Printer_, maker
			FROM product
			WHERE type="Printer"
			GROUP BY maker) AS ps
ON ls.maker = ps.maker;