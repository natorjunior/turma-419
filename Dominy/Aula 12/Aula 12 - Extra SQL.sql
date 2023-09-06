SELECT Departamento, AVG(Salario) AS MediaSalarial
FROM Funcionarios
GROUP BY Departamento;

SELECT Cargo FROM Funcionarios
GROUP BY Cargo;

SELECT F.Nome, F.Cargo, F.Salario
FROM Funcionarios F
INNER JOIN (
    SELECT Departamento, MAX(Salario) AS SalarioMaximo
    FROM Funcionarios
    GROUP BY Departamento
) Subconsulta
ON F.Departamento = Subconsulta.Departamento AND F.Salario = Subconsulta.SalarioMaximo;