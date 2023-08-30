-- VISUALIZAR BASE
SELECT * FROM Funcionarios 

-- VISUALIZAR BASE maior que 1000
SELECT * FROM Funcionarios 
    WHERE 1=1
        AND Salario >= 1000

-- UPDADE NOS VALORES
   UPDATE Funcionarios 
    SET Salario = 1000
    WHERE Salario = 3000