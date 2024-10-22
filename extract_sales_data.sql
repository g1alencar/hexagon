
-- Script SQL para extração de dados do AdventureWorks
SELECT 
    soh.OrderDate,
    soh.TotalDue,
    a.StateProvinceID AS Region,
    p.Name AS Product
FROM 
    Sales.SalesOrderHeader soh
JOIN 
    Sales.SalesOrderDetail sod ON soh.SalesOrderID = sod.SalesOrderID
JOIN 
    Person.Address a ON soh.ShipToAddressID = a.AddressID
JOIN 
    Production.Product p ON sod.ProductID = p.ProductID;
