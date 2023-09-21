import sqlite3
conexao = sqlite3.connect('minha_base.db')
cursor = conexao.cursor()
# Comando SQL para criar uma tabela de exemplo
cursor.execute('''
   CREATE TABLE IF NOT EXISTS pessoas (
       id INTEGER PRIMARY KEY,
       nome TEXT NOT NULL,
       idade INTEGER, 
       cidade TEXT,
       email TEXT UNIQUE
   )
''')
# cursor.execute("INSERT INTO pessoas (nome, idade, cidade, email) VALUES(?,?,?,?)", ("Paula", "20", "Baturité", "p123@email.com"))
#cursor.execute("INSERT INTO pessoas (nome, idade, cidade, email) VALUES(?,?,?,?)", ("Pedero", "22", "Redenção", "p10@email.com"))
cursor.execute("INSERT INTO pessoas (nome, idade, cidade, email) VALUES(?,?,?,?)", ("karen", "18", "Fortaleza", "k@email.com"))




conexao.commit()
conexao.close()
