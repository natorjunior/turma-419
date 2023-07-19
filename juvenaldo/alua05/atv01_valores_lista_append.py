notas = []
while True:
    nota = (input("Digite uma nota ou S para sair: "))
    if nota != "S":
        notas.append(float(nota))
    else:
        break

media = sum(notas)
print(f"A media dos valores digitados é igual a: {(media /len(notas))}")