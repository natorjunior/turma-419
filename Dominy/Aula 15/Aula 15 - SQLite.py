import sqlite3
conexao = sqlite3.connect('minha_base.db')
cursor = conexao.cursor()

def inserir_dados(nome,preco,quantidade):
    cursor.execute("INSERT INTO produtos(nome, preco, quantidade)VALUES(?,?,?)",
                   (nome,preco,quantidade))
    conexao.commit()
def apagar_dados(id):
    cursor.execute("DELETE FROM produtos WHERE id = ?",
                   (id,))
    conexao.commit()
def atualizar_dados(preco,id):
    cursor.execute("UPDATE FROM produtos SET preco = ? WHERE id = ?",
                   (preco,id))
    conexao.commit()
def visualizar_dados():
    consulta = cursor.execute("SELECT * FROM produtos")
    print(consulta.fetchall())
    conexao.commit()

#conexao.execute("""
#                 CREATE TABLE pessoas(id INTEGER PRIMARY KEY, 
#                 nome TEXT NOT NULL,
#                 idade INTEGER NOT NULL,
#                 cidade TEXT NOT NULL)
            
#                 """

#Crie um programa em Python que insira pelo menos 3 registros na tabela "pessoas" com informações fictícias de pessoas.
 
# cursor.executemany("INSERT INTO pessoas(nome,idade,cidade) VALUES (?,?,?);",
# [
#     ("Dominy Martins",27,"Fortaleza"),
#     ("Alan Luz", 39,"Fortaleza"),
#     ("Nator Junior",35, "Fortaleza")
# ]
# )
# cursor.execute("""CREATE TABLE produtos (
#                 id INTEGER PRIMARY KEY,
#                 nome TEXT NOT NULL,
#                 preco FLOAT NOT NULL,
#                 quantidade INTEGER NOT NULL
# )
# """)
while True:

    continuar = int(input(""" Digite a opção que você desejas usar:\n
                      1 = Inserir dados \n
                      2 = Deletar dados \n
                      3 = Atualizar dados \n
                      4 = Visualizar dados \n
                      5 = Sair \n"""))

    if continuar == 1:
        nome = input("Qual o nome do produto? ")
        preco = float(input("Qual o preço do produto? "))
        quantidade = int(input("Qual a quantidade que você está levando? "))
        inserir_dados(nome, preco, quantidade)

    elif continuar == 2:
        id = int(input("Você deseja apagar qual registro? "))
        apagar_dados(id)

    elif continuar == 3:
        preco = float(input("Você deseja alterar o preço do produto para qual valor? "))
        id = int(input("Você deseja atualizar qual registro? "))
        atualizar_dados()
    elif continuar == 4:
        visualizar_dados()
    else:
        break


conexao.commit()
conexao.close()