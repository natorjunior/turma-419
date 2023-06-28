lista = [] 
while True:
    validar = input("Deseja continuar inserindo notas? Digite S para continuar e N para encerrar: ")
    if validar == "S":
        lista.append(float(input("Digite uma nota:")))
        media = sum(lista) / len(lista)

    else:
        a= str(lista).replace('[','').replace(']','') #Remove os colchetes da lista para exibi-la de forma amigável.
        print(f"As notas bimestrais do aluno foram respectivamente {a}. "
              f"A média do aluno foi {media} ")
        break
