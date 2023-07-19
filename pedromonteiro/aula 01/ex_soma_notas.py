lista_notas=[]
while True:
    nota= input("Digite uma nota ou S para sair: ")
    if nota=='S':
        break
    else:
        lista_notas.append(float(nota))
media= sum(lista_notas) / len(lista_notas)

print(media)
