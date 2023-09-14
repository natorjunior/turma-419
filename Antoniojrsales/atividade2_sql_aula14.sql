use db2602;
show tables;
select * from customers;
select state, count(*) as outro_nome
from customers
group by state; 