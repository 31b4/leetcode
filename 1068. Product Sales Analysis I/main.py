# Write your MySQL query statement below
/* Write your T-SQL query statement below */
SELECT p.product_name,s.year,s.price 
from Sales s,Product p 
where p.product_id = s.product_id
