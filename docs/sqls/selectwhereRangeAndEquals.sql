SELECT * 
FROM Customers 
WHERE Country NOT IN ('USA','Germany')
AND CustomerID BETWEEN 50 AND 89
AND City IN ('London');

-- Number of Records: 2