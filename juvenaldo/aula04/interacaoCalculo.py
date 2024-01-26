
print("----------- OPERACAO -----------------")
primeiroValor = int(input("Digite o primeiro valor: "))
segundoVAlor = int(input("Digite o segundo valor: "))

print("1 - SOMA\n"
      "2 - SUBTRACAO\n"
      "3 - MULTIPLICACAO\n"
      "4 - DIVISAO\n"
      "5 - SAIR")
print("----------- OPERACAO -----------------")
operacao = input(" Escolha a opcao de operacao: ")

if operacao == "1" or operacao == "SOMA":
    print(f"O resultado da soma é igual a: {primeiroValor + segundoVAlor}")
if operacao == "2" or operacao =="SUBTRACAO":
    print(f"O resultado da subtração é igual a: {primeiroValor - segundoVAlor}")
if operacao == "3" or operacao == "MULTIPLICACAO":
    print(f"O resultado da multiplicação é igual a: {primeiroValor * segundoVAlor}")
if operacao == "4" or operacao == "DIVISAO":
    print(f"O resultado da multiplicação é igual a: {primeiroValor * segundoVAlor}")
if operacao =="5" or operacao =="SAIR":
    print("Fim operação!")
print("-------- FIM OPERACAO ---------")