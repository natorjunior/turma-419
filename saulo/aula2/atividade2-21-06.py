lista = []

for i in range (1,6):

    valores = int(input("Digite um valor: "))
    lista.append(valores)

soma = lista[2] + lista[3] + lista[4]

print(f"A soma dos 3 últimos valores da lista é {soma}")