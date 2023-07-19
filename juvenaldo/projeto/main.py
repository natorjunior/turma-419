from soma import somar

from subtracao import subtracao

from multiplicacao import  multiplicacao

from divisao import  divisao




resultado = multiplicacao(5,3)
print(resultado)

print("---------------------- TABUADA ------------------\n")
while True:
    operacao = input("Digite uma operacao: ")
    valor1 = int(input("Digite o valor um: "))
    valor2 = int(input("Digite o valor dois: "))
    if operacao == "soma":
        print(somar(valor1, valor2))
    if operacao == "subtracao":
        print(subtracao(valor1, valor2))
    if operacao == "multiplicacao":
        print(multiplicacao(valor1, valor2))
    if operacao == "divisao":
        print(divisao(valor1, valor2))

        print(somar(valor1, valor2))
    condicao= input("Desaja sair: \n"
      "1 - sair\n"
      "2 - continuar")
    if condicao == "1" or condicao == "sair":
        print("sair")
        break
    if condicao == "2" or condicao == "continuar: ":
        print(operacao)



print("--------------- FIM TABUADA ------------------")
