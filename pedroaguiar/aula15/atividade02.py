import sqlite3
conexao = sqlite3.connect('minha_base.db')
cursor = conexao.cursor()
def ver_produtos():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    if not produtos:
        print('Nenhum produto foi encontrado')
    else:
        for produto in produtos:
            print(f"ID:{produto[0]}, Nome:{produto}, Preço:{produto[1]}, Quantidade: {produto[2]}")
def deletar_produtos():
    ver_produtos()
    produtoid = int(input("Digite o ID do produto que deseja deletar:"))
    cursor.execute("DELETE FROM produtos WHERE id=?",(produtoid,))
    conexao.commit()
    print(f"Produto deletado com sucesso!")


cursor.execute('''
    CREATE TABLE if not exists produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        preço FLOAT,
        quantidade INTEGER
    )
''')
while True:
    funcao = input("Escolha: inserir, ver, deletar e exit para sair.): ")
    if funcao.lower() == 'exit':
        break
    elif funcao.lower() =='ver':
        ver_produtos()
    elif funcao.lower() == 'inserir':
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        cursor.execute("INSERT INTO produtos (nome, preço, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
        conexao.commit()
    elif funcao.lower() == 'deletar':
        deletar_produtos()
conexao.close()