create database Paulo_Junior;
use Paulo_Junior;
create table atividade_python(
	id_aula int auto_increment primary key,
    id_nome_aula varchar (50),
    descrição_da_aula varchar (50)
);
insert into atividade_python (id_nome_aula, descrição_da_aula) values 
( 'nome aula1', 'Descrição da aula 1'),
( 'nome aula2', 'Descrição da aula 2'),
('nome aula3', 'Descrição da aula 3'),
( 'nome aula4', 'Descrição da aula 4'),
( 'nome aula5', 'Descrição da aula 5'),
( 'nome aula6', 'Descrição da aula 6'),
( 'nome aula7', 'Descrição da aula 7'),
( 'nome aula8', 'Descrição da aula 8'),
( 'nome aula9', 'Descrição da aula 9'),
( 'nome aula10', 'Descrição da aula 10');

select * from atividade_python;
truncate table atividade_python;
drop table atividade_python;






