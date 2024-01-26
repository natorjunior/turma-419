# Faça um Programa que peça a idade de 5 pessoas,armazene
# a informação no seu respectivo vetor e
# imprima a média da idade.

idade = []
for pessoas in range (5):
    valor = int(input("Digite aqui a sua idade: "))
    idade.append(valor)

print(f"Média das idades de todos as pessoas: {sum(idade) / len(idade)}")
