import sqlite3

conexao = sqlite3.connect('produtos.db')
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE if not exists produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco INTERGER ,
        quantidade TEXT 
    )
''')

def visualizar_lista_produto():
    cursor.execute("SELECT * FROM produtos")
    # Recupera os resultados
    resultados = cursor.fetchall()

    for row in resultados:
        print(row)

def iserir_lista_produtos(nome, preco, quantidade):
    print(nome, preco, quantidade)
    cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))

    conexao.commit()

lista_completa = []

while True:
    opcoes = input('''
Se deseja sair digite [S]air, 
Se deseja visualizar digite [V]isualizar,
Se deseja inserir digite [I]serir,  : ''').lower()
    
    if opcoes == 's':
        break
    elif opcoes == 'v':
        visualizar_lista_produto()
    elif opcoes == 'i':
        nome = input('Digite o nome do produto: ')
        preco = input('Digite o nome do preco: ')
        quantidade = input('Digite o nome do quantidade: ')
        if nome != '' and preco != '' and quantidade != '':
            lista_completa.append((nome, preco, quantidade))
            iserir_lista_produtos(nome, preco, quantidade) 
        
conexao.close()    

