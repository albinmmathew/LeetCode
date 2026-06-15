-- Employees Earning More Than Their Managers

/* Write your PL/SQL query statement below */
select e.name as Employee 
from Employee e 
join Employee e1 
on e.managerId = e1.id
where e.salary>e1.salary