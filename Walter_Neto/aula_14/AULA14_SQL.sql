-- USE WALTER_NETO;
-- CREATE TABLE ATIVIDADE_SQL(
-- 	ID_AULA INT AUTO_INCREMENT KEY,
--     NOME_AULA VARCHAR(50),
--     DESCRICAO_AULA VARCHAR(100)
--     );
    
--     INSERT INTO ATIVIDADE_SQL (NOME_AULA, DESCRICAO_AULA)
--     VALUES('AULA 1', 'SQL.1'), ('AULA 2', 'SQL.2'), ('AULA 3', 'SQL.3'), ('AULA 4', 'SQL.4'), ('AULA 5', 'SQL.5'), 
--     ('AULA 6', 'SQL.6'), ('AULA 7', 'SQL.7'), ('AULA 8', 'SQL.8'), ('AULA 9', 'SQL.9'), ('AULA 10', 'SQL.10')

-- ATIVIDADE 1
-- USE db2602;
-- SHOW TABLES;

-- SELECT * FROM customers
-- 	WHERE 1=1
-- 		AND state = 'RS'

-- ATIVIDADE 2
-- USE db2603;
-- SHOW TABLES;

-- SELECT name, street, city FROM customers
-- 	WHERE 1=1
-- 		AND city = 'Porto Alegre'
--  		GROUP BY NAME, street, city

-- ATIVIDADE 3
USE db2604;
SHOW TABLES;

SELECT * FROM products
	WHERE 1=1 
		AND ((price < 10) OR (price > 100))
