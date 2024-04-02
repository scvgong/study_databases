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

-- supplierid
SELECT Category_GROUP.SupplierID, COUNT(Category_GROUP.SupplierID) CNT 
FROM (SELECT SupplierID, CategoryID, COUNT(CategoryID) CNT 
		FROM Products
		WHERE 1 = 1
		GROUP BY SupplierID, CategoryID
    	) AS Category_GROUP
WHERE 1 = 1
GROUP BY Category_GROUP.SupplierID
ORDER BY COUNT(Category_GROUP.SupplierID) DESC;