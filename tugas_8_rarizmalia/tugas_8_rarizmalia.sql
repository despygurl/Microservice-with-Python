SELECT od.orderNumber, orderDate, customerName, city, country, quantityOrdered, productName 
FROM classicmodels.orders as od, classicmodels.customers, classicmodels.orderdetails, classicmodels.products 
where productName = "1992 Ferrari 360 Spider red" and orderDate between '2004-08-01' and '2004-12-01';