#Crie uma tabela chamada "pessoas" em um banco de dados SQLite. A tabela deve ter as seguintes colunas: "id" (chave primária), "nome", "idade" e "cidade".
#Em seguida, crie um programa em Python que insira pelo menos 3 registros na tabela "pessoas" com informações fictícias de pessoas.

import sqlite3
conexao = sqlite3.connect('minha_base.db')
cursor = conexao.cursor()

conexao.execute("""
                CREATE TABLE pessoas(id INTEGER PRIMARY KEY, 
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                cidade TEXT NOT NULL)
                """)

cursor.executemany("INSERT INTO pessoas(nome,idade,cidade) VALUES (?,?,?);",
[
    ("Dominy Martins",27,"Fortaleza"),
    ("Alan Luz", 39,"Fortaleza"),
    ("Nator Junior",35, "Fortaleza")
]
)

conexao.commit()
conexao.close()