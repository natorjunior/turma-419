from calculadora import soma, subtracao, multiplicacao, divisao

print("Bem-vindo à calculadora!")
print("Escolha a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("0. Sair")

def realizar_operacao(operacao):
    if operacao == "1":
        print("Opção escolhida: Soma!")
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = soma(a, b)
        print(f"Resultado: {resultado}")
    elif operacao == "2":
        print("Opção escolhida: Subtração!")
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = subtracao(a, b)
        print(f"Resultado: {resultado}")
    elif operacao == "3":
        print("Opção escolhida: Multiplicação!")
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = multiplicacao(a, b)
        print(f"Resultado: {resultado}")
    elif operacao == "4":
        print("Opção escolhida: Divisão!")
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        resultado = divisao(a, b)
        print(f"Resultado: {resultado}")
    elif operacao == "0":
        print("Encerrando a calculadora...")
    else:
        print("Opção inválida!")

while True:
    
    operacao = input("Digite o número da operação desejada (ou 0 para sair): ")
    realizar_operacao(operacao)
    if operacao == "0":
        break

