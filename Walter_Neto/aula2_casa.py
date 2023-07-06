#atividade de casa

#inverte numeros

a = int(input('Digite um valor inteiro: '))

def invertido (inver):
    rev = 0
    while inver > 0:
        r = inver % 10
        rev = (rev*10) + r
        inver //= 10
    print(rev)

troca = invertido(a)



#atividade fizz_buzz

a = int(input('Digite um valor inteiro: '))

def fizz_buzz (valor):

    result = valor % 3
    resul2 = valor % 5
    resultf = result + resul2 
    #se for divisivel pelos 3 e 5 a vai somar zeros

    if resultf == 0:
        
        print('FIZZ_BUZZ')

    elif valor % 5:

        print('fizz')

    else:

        print('buzz')

tc = fizz_buzz(a)