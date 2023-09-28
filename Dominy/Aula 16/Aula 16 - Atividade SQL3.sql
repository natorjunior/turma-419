-- use db2605
-- show tables

-- select * from categories;
-- select * from products;
-- select * from providers;

select products.name as produtos , 
       providers.name as fornecedores 
		from products join providers 
                      on providers.id = products.id_providers 
        where id_categories = 6