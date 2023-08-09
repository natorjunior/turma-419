#2 - Peça ao usuário para inserir uma frase e use o método split() para dividir
# a frase em palavras. Em seguida, conte quantas palavras foram inseridas.

frase = input("Digite aqui a frase do dia: ")
palavras = frase.split()
quantidade_palavras = len(palavras)
print(f"A lista {palavras}"f"tem {quantidade_palavras} palavras")
