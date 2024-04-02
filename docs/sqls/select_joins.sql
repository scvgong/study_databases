- Table : Customers, Orders
+ 조건 : CustomerName별로 주문 갯수 표시

SELECT C.CustomerName, COUNT(O.OrderID) AS OrderNumber
FROM Customers C
INNER JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerName
HAVING OrderNumber;

-- 고객 이름별로 주문 개수를 표시하기 위해, 데이터베이스 내에 존재하는 Customers 테이블과 Orders 테이블을 활용하는 것은 매우 중요합니다. 이 두 테이블에는 고객 정보와 주문 정보가 각각 저장되어 있으며, 
-- 이러한 정보를 연결 지어 고객별 주문 개수를 파악할 필요가 있습니다. 이 과정을 위해서는, 두 테이블 간의 관계를 정의하는 CustomerID를 기준으로 조인 작업을 수행해야 합니다. 이렇게 조인된 데이터를 기반으로, 
-- 고객 이름(CustomerName)별로 데이터를 그룹화하고, 이를 통해 각 고객이 얼마나 많은 주문을 했는지를 계산하는 SQL 쿼리를 작성하는 것이 목표입니다.

-- 1. Customers 테이블과 Orders 테이블을 조인합니다. 이 조인 방식은 특히 주문을 하지 않은 고객까지도 결과에 포함시키기 위해 선택되었습니다. 이로 인해, 주문 기록이 없어도 모든 고객이 결과 목록에 나타나며, 
-- 해당 고객의 주문 개수는 0으로 표시됩니다.
-- 2. 주문 개수의 정확한 계산: COUNT(O.OrderID) 함수를 통해 주문 테이블에서 각 고객의 주문 ID(OrderID)를 기준으로 총 주문 개수를 계산합니다. 이 함수는 지정된 조건을 만족하는 행의 수를 반환하여, 고객별 주문 개수를 정확하게 집계합니다.
-- 3. 고객별 그룹화 및 주문 개수 기준 정렬: 결과를 고객 이름(CustomerName)별로 그룹화하여, 각 고객별 주문 개수를 명확히 집계하고, 이를 ORDER BY NumberOfOrders DESC 구문을 사용하여 주문 개수가 많은 고객부터 적은 순으로 정렬합니다. 
-- 이는 사용자가 가장 활발한 구매자부터 확인할 수 있게 해줍니다.
-- 4. 결과에 대한 별칭 사용: AS NumberOfOrders를 사용하여 COUNT(O.OrderID)의 결과에 별칭을 부여합니다. 이는 결과 테이블에서 해당 열의 이름을 NumberOfOrders로 설정하여, 결과를 보다 명확하게 이해할 수 있도록 돕습니다.

- Table : OrderDetails 
+ 조건 : 제품명,가격, 주문 갯수, 고객명 표시

SELECT P.ProductName AS pName, P.Price AS pPrice, OD.Quantity AS quantity, C.CustomerName AS cName
FROM OrderDetails OD
INNER JOIN Products P ON OD.ProductID = P.ProductID
INNER JOIN Orders O ON O.OrderID = OD.OrderID 
INNER JOIN Customers C ON O.CustomerID = C.CustomerID

-- 제품명, 가격, 주문 개수, 고객명을 표시하기 위해서는 단순히 OrderDetails 테이블에서 정보를 조회하는 것만으로는 부족합니다. 이를 위해 Products, Orders, 그리고 Customers 테이블의 데이터를 함께 활용해야 합니다. 
-- 이러한 정보들은 각각 별도의 테이블에 저장되어 있기 때문에, 이들을 효율적으로 연결하기 위해서는 SQL의 조인 연산 기능을 활용하는 것이 필수적입니다.

-- Products 테이블은 제품에 대한 상세 정보를 포함하고 있으며, 여기에는 제품명(ProductName)과 제품의 가격(Price)이 포함됩니다. 이 테이블은 제품의 식별자인 ProductID를 통해 다른 테이블과 관계를 맺습니다.
-- OrderDetails 테이블은 실제 주문된 제품의 수량(Quantity), 제품 식별자(ProductID), 그리고 주문 식별자(OrderID)를 포함하고 있어, 주문과 제품 정보를 연결하는 핵심 역할을 합니다.
-- Orders 테이블은 각 주문의 고유 식별자를 가지고 있으며, 주문을 한 고객의 식별자(CustomerID)를 포함하여 고객 정보와의 연결점을 제공합니다.
-- Customers 테이블은 고객의 이름(CustomerName)을 포함하고 있어, 고객 개인의 정보를 관리합니다.
-- 이 정보들을 연결하여 조회하기 위해, SQL 쿼리는 INNER JOIN 연산자를 사용하여 OrderDetails, Products, Orders, 그리고 Customers 테이블을 적절히 조인합니다. 
-- 이 과정을 통해, 각 테이블에서 필요한 정보를 추출하고 결합하여, 최종적으로 제품명, 가격, 주문 개수, 고객명을 하나의 결과로 표시합니다.

-- 1. 먼저, OrderDetails와 Products를 ProductID를 기준으로 내부 조인하여, 주문된 각 제품의 이름과 가격 정보를 가져옵니다.
-- 2. 이렇게 얻은 결과를 다시 Orders 테이블과 내부 조인하여, 각 주문의 고객 식별자를 매핑합니다. 이를 통해 주문과 고객 간의 연결을 확립합니다.
-- 3. 마지막으로, Customers 테이블과의 내부 조인을 통해, 각 주문을 한 고객의 이름을 최종 결과에 추가합니다.

- Table : Orders
+ 조건 : 가장 많이 주문 받은 회사 직원명과 갯수

SELECT E.LastName, E.FirstName, COUNT(O.OrderID) AS OrderCount
FROM Orders O
INNER JOIN Employees E ON O.EmployeeID = E.EmployeeID
GROUP BY E.EmployeeID
ORDER BY COUNT(O.OrderID) DESC
LIMIT 1;

-- 가장 많이 주문 받은 회사 직원의 이름과 그가 받은 주문의 개수를 찾기 위해서는 Orders 테이블과 직원 정보를 담고 있는 테이블(예를 들어, Employees 테이블)을 조인해야 합니다. 
-- 그리고 주문을 가장 많이 받은 직원을 찾기 위해 SQL의 GROUP BY와 ORDER BY 절을 사용하며, 집계 함수 COUNT()를 사용하여 각 직원별로 받은 주문의 수를 계산합니다.

-- 다음은 이러한 요구 사항을 만족하는 SQL 쿼리의 예시입니다. 이 예시는 Employees 테이블이 EmployeeID를 통해 직원 정보를 저장하고 있으며, 
-- Orders 테이블이 주문을 담당한 직원의 식별자를 EmployeeID로 참조하고 있다고 가정합니다.

-- 1. Orders 테이블과 Employees 테이블을 EmployeeID를 기준으로 내부 조인하여, 각 주문에 대한 담당 직원의 정보를 가져옵니다.
-- 2. GROUP BY 절을 사용하여 결과를 EmployeeID별로 그룹화합니다. 이렇게 하면 각 직원별로 주문 받은 횟수를 계산할 수 있습니다.
-- 3. COUNT() 함수를 사용하여 각 그룹(즉, 각 직원)별로 주문의 총 개수를 계산합니다.
-- 4. ORDER BY 절을 사용하여 계산된 주문 개수를 기준으로 결과를 내림차순으로 정렬합니다. 이렇게 하면 가장 많은 주문을 받은 직원이 결과의 맨 위에 위치하게 됩니다.
-- 5. LIMIT 1을 사용하여 결과의 상위 1개의 행만을 반환합니다. 이는 가장 많은 주문을 받은 직원의 이름과 그가 받은 주문의 개수만을 보여줍니다.