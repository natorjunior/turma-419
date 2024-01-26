import statistics
notas = []
while True:

    validar = input("Deseja continuar inserindo notas(S/N): ")
    if validar == "N":
        print(f"As notas dos alunos são, respectivamente {notas}")
        print(f"A média é {media}")
        break

    elif validar == "S":
        notasadd = int(input("Digite as notas dos alunos: "))
        notas.append(notasadd)
        media = statistics.mean(notas)
    else:
        print("Digite conforme solicitado (S/N)")
