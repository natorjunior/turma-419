lista = []
contador = 1
while contador <= 4:
    numero = int(input('Digite um numero: '))
    contador = contador + 1
    lista.append((numero))
soma = sum(lista)
resultado = soma / 4
print(f'A media do das 4 notas foram {resultado}')

