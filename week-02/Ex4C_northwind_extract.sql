/* 
4.a) The name of the table that holds the items Northwind sells is table products.
4.b) The name of the table that holds the types/categories of the items Northwind sells is table categories.
*/

SELECT * FROM employees; -- 5.a) The Northwind employee whose name makes it look like she's a bird is employee on row 4 (Employee ID 4) which is Peackock Margaret.
SELECT * FROM products; -- 6.a) This query returns 77 rows.
/*  On the dropdrown menu I selected on "Limit to 10 rows" to only retrieve 10 rows. 
BONUS: I used this link https://www.w3schools.com/sql/sql_top.asp to determine how to write a query to limit the number of rows returned. 
It showed the example below, but I modified it so it returns fill rows, not just a specific column.

SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;
*/

SELECT * FROM products LIMIT 5; 
SELECT * FROM categories; -- The category ID for seafood is ID 8. 

