SELECT CustomerName 
FROM Customers
WHERE CustomerID IN (SELECT CustomerID
                    FROM Orders
                    GROUP BY CustomerID
                    HAVING COUNT(OrderID) >= 5);

SELECT EmployeeID, Notes
FROM Employees
WHERE EmployeeID IN (SELECT EmployeeID 
					FROM Orders
					GROUP BY EmployeeID
					HAVING COUNT(EmployeeID) >= 20
                    ORDER BY EmployeeID ASC);
