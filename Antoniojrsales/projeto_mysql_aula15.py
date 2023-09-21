import sqlite3

conexao = sqlite3.connect('pessoas_um.db')
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE if not exists pessoas_um (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTERGER UNIQUE,
        cidade TEXT UNIQUE
    )
''')

# cursor.execute("drop table pessoas_um")

cursor.execute("INSERT INTO pessoas_um (nome, idade, cidade) VALUES (?, ?, ?)", ('Alice', 'Alice@gmail.com', 'Fortaleza'))
cursor.execute("INSERT INTO pessoas_um (nome, idade, cidade) VALUES (?, ?, ?)", ('Maria', 'Maria@gmail.com', 'Recife'))
cursor.execute("INSERT INTO pessoas_um (nome, idade, cidade) VALUES (?, ?, ?)", ('Jose', 'Jose@gmail.com', 'Salvador'))

#cursor.execute("DELETE FROM pessoas WHERE nome = ?", ('Jose',))


conexao.commit()
conexao.close()