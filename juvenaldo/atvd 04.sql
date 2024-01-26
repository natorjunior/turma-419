create database JUVENALDO_CANJA;

use JUVENALDO_CANJA;


create table atividades_python(
	id_aula int auto_increment primary key,
    nome_aula varchar (50),
    descricao_da_aula varchar (40)
);

insert into 
	atividades_python (nome_aula, descricao_da_aula) 
values
	("Consultas em SQL", "Comandos básicos em SQL"),
    ("Funções", "Como utilizar funções do Python"),
    ("Biblioteca", "O que é?"),
    ("Lista", "Como introduzir dados em uma lista"),
    ("R", "R como linguagem de programação"),
    ("Agricolae", "Pacote agricolae no R"),
    ("Infinity", "Centro de referencia"),
    ("CSS", "Estilos"),
    ("HTML", "Marcação");

use db2603;
show tables;
select * from customers;
select * from customers where city = "Porto Alegre"; 

use db2602;
show tables;
select * from customers;
SELECT * FROM customers where state = "RS";