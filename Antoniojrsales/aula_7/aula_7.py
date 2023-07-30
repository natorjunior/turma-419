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

def usuario_idade(nome_usuario):
    if nome_usuario in nome_existentes:
        print('Nome existe na lista')
        return usuarios[nome_usuario]['idade']
    else:
        return('Nome nao existe na lista')

def exibir_texto():
   caixa_texto_nome = caixa_texto.get()
   idade = usuario_idade(caixa_texto_nome)
   print("Texto inserido:", idade)
   rotulo2.config(text=idade)

def deleta_texto():
   caixa_texto_nome = caixa_texto.delete(0, END)


janela = Tk()
janela.title("aula_07_tkinter")
janela.geometry("300x200")
rotulo = Label(janela, text="Digite sua mensagem")
rotulo.pack()
caixa_texto = Entry(janela)
caixa_texto.pack()
botao = Button(janela, text="Exibir Texto", command=exibir_texto)
botao.pack()
botao2 = Button(janela, text="Deletar Texto", command=deleta_texto)
botao2.pack()
rotulo2 = Label(janela, text="")
rotulo2.pack()

janela.mainloop()