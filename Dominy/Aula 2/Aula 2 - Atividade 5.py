# Faça um programa que simule um lançamento de dados. Lance
# o dado 100 vezes e armazene os resultados em uma lista.
# Depois, mostre quantas vezes cada valor foi conseguido. Dica:
# use uma lista de contadores(1-6) e uma função para gerar
# números aleatórios, simulando os lançamentos dos dados.

import random  # Usandom a biblioteca de aleatoriedade do python

lista_dados = []  # criando a lista vázia


# Uma função é um pedaco de código que só irá ser realizado quando eu chama-la pelo nome
def lancamentos():
    for i in range(1, 101):
        numero_aleatorio = random.randint(1,
                                          6)  # Função que gera um número aleatorio entre 1 até 6 (poderia aumentar esse intervalo sem problema)
        lista_dados.append(numero_aleatorio)  # Adicioando o número a lista


lancamentos()  # O laço só irá ser ativado quando o python ler essa linha
# Chamamento da função
print(lista_dados)

# Variaveis que armazenaram o número toda vez que aparecer
numero_1 = []
numero_2 = []
numero_3 = []
numero_4 = []
numero_5 = []
numero_6 = []

# Laço de repetição para percorrer cada elemento da lista
for i in lista_dados:
    # Se ele for igual a um número de 1 até 6 adicionarei o elemento a sua respectiva lista
    if i == 1:
        numero_1.append(1)
    elif i == 2:
        numero_2.append(2)
    elif i == 3:
        numero_3.append(3)
    elif i == 4:
        numero_4.append(4)
    elif i == 5:
        numero_5.append(5)
    elif i == 6:
        numero_6.append(6)

    # Função sum(), faz a soma dos valores númericos de uma lista
print('O total de vezes que o 1 apareceu foi', len(numero_1))
print('O total de vezes que o 2 apareceu foi', len(numero_2))
print('O total de vezes que o 3 apareceu foi', len(numero_3))
print('O total de vezes que o 4 apareceu foi', len(numero_4))
print('O total de vezes que o 5 apareceu foi', len(numero_5))
print('O total de vezes que o 6 apareceu foi', len(numero_6))