from operacoes import somar, subtrair, multiplicar, dividir
while True:
        print('---------Operacoes------------------')
        print('1 - soma\n'
              '2 - subtracao\n'
              '3 - divisao\n'
              '4 - multiplicacao\n'
              '5 - fim\n')
        operacao = input('Digite a operacao: ')
        if operacao == '5' or operacao == 'fim':
            print('fim')
            break
        else:
            print('-----------Numeros------------------')
            numeroUm = int(input('Digite um valor: '))
            numeroDois = int(input('Digite outro valor: '))
            print('----------------------------------\n')

            print('-----------Resultado--------------\n')
            if operacao == '1' or operacao == 'soma' or operacao == '+' :
                print(f'O valor {numeroUm} + {numeroDois} = {somar(numeroUm, numeroDois)}')
            elif operacao == '2' or operacao == 'subtracao' or operacao == '-' :
                print(f'O valor {numeroUm} - {numeroDois} = {subtrair(numeroUm, numeroDois)}')
            elif operacao == '3' or operacao == 'divisao' or operacao == '/' :
                print(f'O valor {numeroUm} / {numeroDois} = {dividir(numeroUm, numeroDois)}')
            elif operacao == '4' or operacao == 'divisao' or operacao == '*' :
                print(f'O valor {numeroUm} x {numeroDois} = {multiplicar(numeroUm, numeroDois)}')
            elif operacao == '5' or operacao == 'fim' :
                print('fim')
                break
            else:
                print('Dados invalidos favor digitar os valores corretos')