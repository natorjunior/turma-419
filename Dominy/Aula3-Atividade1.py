print("Escreva um programa que solicite ao usuário que digite uma série de notas e, \n "
      "em seguida, calcule e exiba a média das notas fornecidas.")

notas = []
while True:
    serie = int(input("Digite sua nota aqui: "))
    notas.append(serie)
    valor = int(input("Você deseja sair?\n"
                  "1 - Continuar\n"
                  "0 - Sair\n"))
    if valor == 0:
        print(f"A média das suas notas é: {sum(notas) / len(notas)}")
        break

