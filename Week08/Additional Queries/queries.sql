SELECT e.FirstName, e.LastName, SUM(od.UnitPrice)
FROM employees AS e
LEFT JOIN orders on orders.EmployeeID=e.employeeID
LEFT JOIN "order details" AS od on orders.orderID=od.OrderID
GROUP BY e.employeeID;

SELECT *
FROM products
ORDER BY UnitPrice DESC
LIMIT 10;

SELECT categories.categoryName, COUNT(products.ProductID)
FROM products
JOIN categories ON products.CategoryID=categories.CategoryID
GROUP BY categories.categoryID;

SELECT p.ProductName
FROM products AS p
JOIN "order details" AS od ON p.ProductID=od.ProductID
GROUP BY p.productID
ORDER BY COUNT(od.OrderID) DESC
LIMIT 5;

/*SELECT o.orderID, p.ProductName, e.FirstName, e.LastName
FROM products AS p
JOIN "order details" AS od ON p.ProductID=od.ProductID
JOIN orders AS o ON o.OrderID=od.OrderID
JOIN employees AS e ON o.EmployeeID=e.EmployeeID
WHERE o.OrderDate > "1996-06-16" AND o.orderDate < "1996-09-26";*/


SELECT e.FirstName, e.LastName, r.RegionDescription
FROM employees AS e
JOIN employeeterritories AS et ON et.EmployeeID=e.EmployeeID
JOIN territories AS t ON t.TerritoryID=et.TerritoryID
JOIN region AS r ON r.RegionID=t.RegionID
JOIN orders AS o ON o.EmployeeID=e.EmployeeID
JOIN "order details" AS od ON od.OrderID=o.OrderID
JOIN products AS p ON p.ProductID = od.ProductID
GROUP BY e.EmployeeID
ORDER BY COUNT(o.OrderID) DESC
LIMIT 5;