notas = []
quantidade = int(input("Digite a quantidade de notas:"))
for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = sum(notas)/ len(notas)
print("A média das notas é:", media)
