lista = []
# for i in range(0,4):
while True:
    validar = input("Deseja continuar inserindo notas? Digite S para continuar e N para encerrar: ")
    if validar == "S":
        lista.append(float(input("Digite uma nota:")))
        media = sum(lista) / len(lista)

    else:
        a= str(lista).replace('[','').replace(']','')
        print(f"As notas bimestrais do aluno foram respectivamente {a}. "
              f"A média do aluno foi {media} ")
        break
