/* 1- Escreva uma consulta SQL para calcular a média salarial por departamento. Apresente o resultado com o nome do departamento e a média salarial.*/
SELECT Departamento, AVG(Salario) AS MediaSalarial
FROM Funcionarios
GROUP BY Departamento;
/* 2- Escreva uma consulta para mostrar todos os cargos existentes na tabela, sem que ocorra duplicidade.  */
SELECT Cargo FROM Funcionarios
GROUP BY Cargo;

/* 3- Escreva uma consulta SQL para encontrar os funcionários com os salários mais altos em cada departamento. Apresente o nome, cargo e salário de cada funcionário.*/
SELECT F.Nome, F.Cargo, F.Salario
FROM Funcionarios F
INNER JOIN (
    SELECT Departamento, MAX(Salario) AS SalarioMaximo
    FROM Funcionarios
    GROUP BY Departamento
) Subconsulta
ON F.Departamento = Subconsulta.Departamento AND F.Salario = Subconsulta.SalarioMaximo;
