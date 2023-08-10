import tkinter as tk
#---------------------------------FUNÇÕES----------------------------------
def print_label(texto_do_botao):
    concatena = str_global_tela.get()+texto_do_botao
    str_global_tela.set(concatena)
    tela.config(text=str_global_tela.get())

def limpar ():
    str_global_tela.set('')
    tela.config(text=str_global_tela.get())

def operacoes():
    tela.config(text=eval(str_global_tela.get()))

#---------------------------------INTERFACE--------------------------------
janela = tk.Tk()
str_global_tela = tk.StringVar()
str_global_tela.set('')

tela = tk.Label(janela, text = "Calculadora do Dominy", height= 7,width= 30)

#numeros da calculadora
number0 = tk.Button(janela,text= 0, bg="yellow",width=10, command=lambda: print_label('0'))
number1 = tk.Button(janela,text= 1, bg="yellow",width=10, command=lambda: print_label('1'))
number2 = tk.Button(janela,text= 2, bg="yellow",width=10, command=lambda: print_label('2'))
number3 = tk.Button(janela,text= 3, bg="yellow",width=10, command=lambda: print_label('3'))
number4 = tk.Button(janela,text= 4, bg="yellow",width=10, command=lambda: print_label('4'))
number5 = tk.Button(janela,text= 5, bg="yellow",width=10, command=lambda: print_label('5'))
number6 = tk.Button(janela,text= 6, bg="yellow",width=10, command=lambda: print_label('6'))
number7 = tk.Button(janela,text= 7, bg="yellow",width=10, command=lambda: print_label('7'))
number8 = tk.Button(janela,text= 8, bg="yellow",width=10, command=lambda: print_label('8'))
number9 = tk.Button(janela,text= 9, bg="yellow",width=10, command=lambda: print_label('9'))

#operadores matemáticos
adicao = tk.Button(janela,text= "+", bg="red",width=10, command=lambda: print_label('+'))
subtracao = tk.Button(janela,text= "-", bg="red",width=10, command=lambda: print_label('-'))
divisao = tk.Button(janela,text= "/", bg="red",width=10, command=lambda: print_label('/'))
multiplicacao = tk.Button(janela,text= "*", bg="red",width=10, command=lambda: print_label('*'))

#apagar e resultado
deletar = tk.Button(janela,text= "c", bg="blue",width=10, command= limpar)
resultado = tk.Button(janela,text= "=", bg="blue",width=10, command= operacoes)

tela.grid(row=0 , column=0, columnspan=4)

number1.grid(row=1, column=0, padx=2, pady=3)
number2.grid(row=1, column=1, padx=2, pady=3)
number3.grid(row=1, column=2, padx=2, pady=3)
number4.grid(row=2, column=0, padx=2, pady=3)
number5.grid(row=2, column=1, padx=2, pady=3)
number6.grid(row=2, column=2, padx=2, pady=3)
number7.grid(row=3, column=0, padx=2, pady=3)
number8.grid(row=3, column=1, padx=2, pady=3)
number9.grid(row=3, column=2, padx=2, pady=3)
number0.grid(row=4, column=1, padx=2, pady=3)

adicao.grid(row=1, column=3, padx=2, pady=3)
subtracao.grid(row=2, column=3, padx=2, pady=3)
multiplicacao.grid(row=3, column=3, padx=2, pady=3)
divisao.grid(row=4, column=3, padx=2, pady=3)

deletar.grid(row=4, column=0, padx=2, pady=3)
resultado.grid (row=4, column=2, padx=2, pady=3)

janela.mainloop()

