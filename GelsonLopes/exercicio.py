# nota1 = int(input("Digite 1ª Nota: "))
# nota2 = int(input("Digite a 2ª Nota: "))
# nota3 = int(input("Digite a 3ª Nota: "))
# nota4 = int(input("Digite a 4ª Nota: "))

# notas = [nota1, nota2, nota3, nota4]
# media = (nota1 + nota2 + nota3 + nota4) / 4 

# print("Suas Notas foram: ", notas, "Sua média é: ", media)

notas = []

for i in range (0,4): 
    nota = int(input(f"Digite a {i+1}ª "))
    notas.append (nota)

print("Sua nota",nota)

lista1 = []
lista2 = []

for i in range(0,3):
    primeiro = int(input(f"Escolha 3 Números: {i+1} ª" ))
    lista1.append (primeiro)

for i in range(0,3):
    segundo =  int(input(f"Escolha mais 3 Números: {i+1} ª"))
  
    lista2.append (segundo)

soma = lista1[0] + lista2[-1]

print("A soma é: ", soma)
