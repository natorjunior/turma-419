#Atividade1

#dicionario = {}

#for i in range (1,4):
   # nome = str(input('Informe o nome: '))
   # nota = float(input('Informe a nota: '))
   # dicionario[nome] = nota

#maior = (max(dicionario.values()))

#print(*filter(lambda nome:maior <= dicionario[nome],dicionario))

#print(sum(dicionario.values()) / len(dicionario.values()))


#Atividade 2



##retorna hello word
#def proced (proc1):
  #  total = proc1
  #  return ('Hello World')
#recebe = print(proced (1))


##retorna o que digita
#def proced (vr):
 #   print (vr)

#proced(vr = input('Digite: '))



##recebe e calcula area
#a = float(input ('Digite o comprimento: '))
#b = float(input ('Digite a largura: '))


#def valor_area (base,altura):
 #   total = base * altura
 #   return total
#area = valor_area (b,a)
#print(area)



##retorna o menor 

par_1 = float(input ('Digite: '))
par_2 = float(input ('Digite: '))

def valores (valor1,valor2):
    if valor1<valor2:
        print (valor1)
    elif valor1<valor2:
        print(valor2)
    else:
        print('Iguais') 
final = valores(par_1,par_2)
print(final)







