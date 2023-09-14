create database antonio_sales_junior;
use antonio_sales_junior;
CREATE DATABASE IF NOT EXISTS antonio_sales_junior;
create table Atividade_Python(
Id_aula int auto_increment primary key,
Nome_Aula VARCHAR(50),
Descricao_Aula VARCHAR(50)
);
insert into Atividade_Python( Nome_Aula, Descricao_Aula)
values ('Aula1', 'Git GitHub'),       
		('Aula2', 'Fatiamento de Lista'),
       ('Aula3', 'Dicionarios'),
       ('Aula4', 'Funcoes'),
       ('Aula5', 'MQTT'),
       ('Aula6', 'Revisao Git GitHub'),
       ('Aula7', 'Tkinter'),
       ('Aula8', 'Tkinter Projeto'),
       ('Aula9', 'Split Map'),
       ('Aula10', 'POO');

select * from Atividade_Python;

