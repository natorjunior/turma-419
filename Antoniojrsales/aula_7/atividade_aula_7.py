from tkinter import *
usuarios = {'maria' : {'idade':40 , 'altura':'1,70'}, 
            'junior' : {'idade':43 , 'altura':'1,80'},
            'iasmim' : {'idade':12 , 'altura':'1,70'},
            'joao' : {'idade':6 , 'altura':'1,40'},
            'miguel' : {'idade':8 , 'altura':'1,45'},
            'kk' : {'idade':38 , 'altura':'1,65'},
            'alda' : {'idade':63 , 'altura':'1,50'},
            'carlos' : {'idade':60 , 'altura':'1,70'},
            'luis' : {'idade':35 , 'altura':'1,60'},
            'patricia' : {'idade':30 , 'altura':'1,50'},
            }
nome_existentes = list(usuarios)

def usuario_idade():
    nome_usuario = str(input('Digite o nome desejado: '))
    if nome_usuario in nome_existentes:
        print('Nome existe na lista')
        return usuarios[nome_usuario]['idade']
    else:
        return('Nome nao existe na lista')

print(usuario_idade())