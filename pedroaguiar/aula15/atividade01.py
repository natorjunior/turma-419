import sqlite3
conexao = sqlite3.connect('minha_base.db')
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE if not exists pessoas (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        cidade TEXT
    )
''')
cursor.execute("INSERT INTO pessoas (nome, idade, cidade) VALUES (?, ?, ?)", ('Pedro', 30, 'Fortaleza'))
cursor.execute("INSERT INTO pessoas (nome, idade, cidade) VALUES (?, ?, ?)", ('João', 29, 'Fortaleza'))
cursor.execute("INSERT INTO pessoas (nome, idade, cidade) VALUES (?, ?, ?)", ('Debora', 35, 'Canoa Quebrada'))
cursor.execute("INSERT INTO pessoas (nome, idade, cidade) VALUES (?, ?, ?)", ('Joaquim', 37, 'Canoa Quebrada'))


conexao.commit()
conexao.close()