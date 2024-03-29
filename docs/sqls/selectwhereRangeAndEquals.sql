-- 1번째 조건
SELECT * 
FROM Customers 
WHERE Country NOT IN ('USA','Germany');
-- Number of Records: 67

-- 2번째 조건
SELECT * 
FROM Customers 
WHERE CustomerID BETWEEN 50 AND 89
AND City = 'London';
-- Number of Records: 67