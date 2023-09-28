-- USE db2609
-- SHOW TABLES
SELECT categories.name, 
	   sum(products.amount) as soma_quantidade 
                       FROM categories join products
					   on products.id_categories = categories.id 
					   group by categories.name;




