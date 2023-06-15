#lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#print(f"Exemplo de lista {list} ")
print("----------------------- Dados do aluno --------------------\n")
aluno = input("Digite aqui os dados do aluno: ")
print("----------------------- Dados das notas dos alunos --------------------\n")
lista = []
for contador in range (0,4):
    valor = int(input("Digite aqui as 4 notas do aluno: \n"))
    lista.append(valor)
    print(f"Lista de todas as notas do aluno {lista}\n")
media = (lista[0] + lista[1] + lista[2] + lista[3]) / 4
print(f"A média do {aluno} é {media}")
