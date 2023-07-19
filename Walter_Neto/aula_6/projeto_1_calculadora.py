#calculadora
# divisao.py
def divisao(a,b):
   return a/b

# multiplicar.py
def multiplicar(a,b):
   return a * b

# somar.py
def somar(a,b):
   return a + b

# subtrair.py
def subtrair(a,b):
   return a - b



from somar import somar
from subtrair import subtrair
from multiplicar import multiplicar
from divisao import divisao

valor_1 = float(input("Digite um número: "))
operacao = input("Qual operação deseja: ")
valor_2 = float(input("Digite um número: "))


if operacao == "+":
    resultado = somar(valor_1,valor_2)
    print(int(resultado))
elif operacao == "-":
    resultado = subtrair(valor_1,valor_2)
    print(int(resultado))
elif operacao == "*":
    resultado = multiplicar(valor_1,valor_2)
    print(int(resultado))
elif operacao == "/":
    resultado = divisao(valor_1,valor_2)
    print(int(resultado))
else:
    print("Operação Inválida")

