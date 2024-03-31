-- 첫번째 조건
-- - Table : Products
-- + 조건 : CategoryID 가 10개 이상
SELECT * FROM Products
WHERE CategoryID >= 10;
-- Number of Records: 0

-- 두번째 조건
-- Table : Customers, Orders
-- 조건 : 주문 갯수가 5개 이상인 CustomerName 찾기
SELECT CustomerName 
FROM Customers
WHERE CustomerID IN (SELECT CustomerID
                    FROM Orders
                    GROUP BY CustomerID
                    HAVING COUNT(OrderID) >= 5);

-- Number of Records: 9