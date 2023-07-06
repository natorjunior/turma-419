#Escreva uma função que recebe dois parâmetros e imprime o menor dos dois.
# Se eles forem iguais, imprima que eles são iguais.

def test(valor1,valor2):
    if valor1 < valor2:
        print(valor1)
    elif valor2 < valor1:
        print(valor2)
    else:
        print("Os valores são iguais!")

test(10,50)