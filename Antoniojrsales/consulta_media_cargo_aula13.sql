SELECT distinct(Departamento) FROM Funcionarios;

SELECT AVG(Salario) FROM Funcionarios where Departamento = 'TI';

SELECT AVG(Salario) FROM Funcionarios where Departamento = 'RH';

SELECT AVG(Salario) FROM Funcionarios where Departamento = 'Finanças';

SELECT AVG(Salario) FROM Funcionarios where Departamento = 'Design'