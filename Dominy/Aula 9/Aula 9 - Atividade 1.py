#1 - Crie uma lista de temperaturas em graus Celsius e use a função map() para converter
# essas temperaturas para graus Fahrenheit. A fórmula de conversão é:
# Fahrenheit = Celsius * 9/5 + 32.
lista_celsius = [25,26,28,30,35,40]
def fahrenheit(c):
    celsius = (c * 9)/5 + 32
    return celsius

lista_fahrenheit = list(map(fahrenheit,lista_celsius))
print(lista_fahrenheit)






