##testes para utilizar
# frase = "2023-08-09"
# ano,mes,dia = frase.split("-")  # O separador padrão é o espaço em branco
# print(f"Ano: {ano}, Mês: {mes}, Dia: {dia}")

##testes para utilizar
# def conversao_f (a):
#     fahr = a * 1.8 + 32
#     return fahr

# lista = [25,15,12]

# lista_f = list(map(conversao_f,lista))
# print (lista_f)


from tkinter import *

def font_p ():
    return "Arial 15"

def background_centro ():
    return "#F6F4EB"

def background_botao ():
    return "#4682A9"

def background_janela ():
    return "#749BC2"

def background_espe ():
    return "#91C8E4"

def background_apaga ():
    return "#749BC2"


janela = Tk()
janela.configure(bg=background_janela())
janela.title("Calculadora")
janela.geometry("348x280")

enter = Label(janela,width=23,height=5,bg=background_centro(),font=font_p(), padx=1)
enter.grid(row=0, column=0, columnspan=15)


#botoes

# botao = Button(janela,text=("7"),width=7,bg=background_botao,font=font_p,)
# botao.grid(row=1, column=1)


botao = []

for i in range(10):
    botaox = Button(janela, text=(i),width=7,bg=background_botao(),font=font_p())
    botao.append(botaox) 

botao[0].grid(row=4, column= 1)
botao[1].grid(row=3, column= 0)
botao[2].grid(row=3, column= 1)
botao[3].grid(row=3, column= 2)
botao[4].grid(row=2, column= 0)
botao[5].grid(row=2, column= 1)
botao[6].grid(row=2, column= 2)
botao[7].grid(row=1, column= 0)
botao[8].grid(row=1, column= 1)
botao[9].grid(row=1, column= 2)

botao_mul = Button(janela,text=("x"),width=7,bg=background_espe(),font=font_p())
botao_mul.grid(row=1, column=3)

botao_div = Button(janela,text=("/"),width=7,bg=background_espe(),font=font_p())
botao_div.grid(row=2, column=3)

botao_sum = Button(janela,text=("+"),width=7,bg=background_espe(),font=font_p())
botao_sum.grid(row=3, column=3)

botao_result = Button(janela,text=("="),width=7,bg=background_espe(),font=font_p())
botao_result.grid(row=4, column=3)

botao_apagar = Button(janela,text=("C"),width=7,bg=background_apaga(),font=font_p())
botao_apagar.grid(row=4, column=0)

botao_dim = Button(janela,text=("-"),width=7,bg=background_espe(),font=font_p())
botao_dim.grid(row=4, column=2)



janela.mainloop()