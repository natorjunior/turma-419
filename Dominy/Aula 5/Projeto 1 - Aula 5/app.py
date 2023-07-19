#importando funções
from funcoes import *

#Menu para calculadora
valor1 = float(input("Digite o primeiro valor: "))
operacao = int(input("1 - Subtrair \n"
                 "2 - Somar\n"
                 "3 - Dividir\n"
                 "4 - Multiplicar\n"
                 "Qual operação matematica você quer usar? "))
valor2 = float(input("Digite o primeiro valor: "))

if operacao == 1 or operacao == "-":
    resultado = subtrair(valor1,valor2)
elif operacao == 2 or operacao == "+":
    resultado = somar(valor1,valor2)
elif operacao == 3 or operacao == "/":
    resultado = dividir(valor1,valor2)
elif operacao == 4 or operacao == "*":
    resultado = multiplicar(valor1, valor2)
else:
    print("Operação Inválido")
print(resultado)




