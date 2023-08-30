1. Escreva uma consulta SQL para selecionar todos os registros da tabela "Funcionarios";

select * from Funcionarios

2. Escreva uma consulta SQL para encontrar o nome e cargo dos funcionários cujo o salário seja maior ou igual 1000.

select nome,cargo from Funcionarios 
where salario >= 1000

3. Escreva uma consulta SQL para atualizar o salário dos funcionários, aqueles que recebem até 2000 devem receber 3000.

update funcionarios set salarios = 3000
where salarios <= 2000