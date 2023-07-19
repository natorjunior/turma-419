
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))
n4 = int(input("Digite a quarta nota: "))

media = print(f"A media é igual a: {(n1+n2+n3+n4)/4}")

lista = [n1,n2,n3,n4]
print(lista)

from statistics import mean

print(mean(lista))
print("--------------FIM LISTA -----------------------\n"
      "lista\n"
      "\n"
      "\n"
      "")