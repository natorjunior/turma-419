import sqlite3
conexao = sqlite3.connect('atividade2_produtos.db')
cursor = conexao.cursor()
# Comando SQL para criar uma tabela de exemplo
cursor.execute('''
   CREATE TABLE IF NOT EXISTS produtos (
       id INTEGER PRIMARY KEY,
       nome TEXT NOT NULL,
       preco FLOAT, 
       quantidade INTEGER
   )
''')

def inserir (nome, preco, quantidade):
    cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES(?,?,?)", (nome, preco, quantidade))
# inserir("George", 10, 4)

while True:
    nome_Produto = input("Digite o nome do produto: ")
    precoProduto = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade: "))
    inserir(nome_Produto,precoProduto,quantidade)
    sair = input("Deseja sair? ")
    if sair == "SIM":
        break
   
cursor.execute("DELETE FROM produtos WHERE id = ?", (3,))
cursor.execute("UPDATE produtos SET nome = ? WHERE id = ?", ("quinoa", 7))
cursor.execute("SELECT * FROM produtos")
resultados = cursor.fetchall()
print(resultados)
for row in resultados:
   print(row)
conexao.commit()
conexao.close()