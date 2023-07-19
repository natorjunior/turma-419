from somar import somar
from subtrair import subtrair
from multiplicar import multiplicar
from dividir import dividir

while True:
    validar = input("Deseja calcular? S-sim N-não: ")
    if validar == "S" or validar == "s" or validar == "sim":
        operacao = int(input("Informe qual operação deseja realizar \n"
                        "1 - soma "
                        "2 - subtracão "
                        "3 - multiplicação "
                        "4 - divisão: "))
        if operacao == 1:
            numeroa = int(input("Informe o primeiro número: "))
            numerob = int(input("Informe o segundo número: "))
            resultado = somar(numeroa, numerob)
            print(resultado)


        if operacao == 2:
            numeroa = int(input("Informe o primeiro número: "))
            numerob = int(input("Informe o segundo número: "))
            resultado = subtrair(numeroa, numerob)
            print(resultado)

        if operacao == 3:
            numeroa = int(input("Informe o primeiro número: "))
            numerob = int(input("Informe o segundo número: "))
            resultado = multiplicar(numeroa, numerob)
            print(resultado)

        if operacao == 4:
            numeroa = int(input("Informe o primeiro número: "))
            numerob = int(input("Informe o segundo número: "))
            resultado = dividir(numeroa, numerob)
            print(resultado)
    else:
        break