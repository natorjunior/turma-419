import tkinter as tk
janela = tk.Tk()

tela = tk.Label(janela, text = "Calculadora do Dominy", height= 7,width= 30)

#numeros da calculadora
number0 = tk.Button(janela,text= 0, bg="yellow",width=10)
number1 = tk.Button(janela,text= 1, bg="yellow",width=10)
number2 = tk.Button(janela,text= 2, bg="yellow",width=10)
number3 = tk.Button(janela,text= 3, bg="yellow",width=10)
number4 = tk.Button(janela,text= 4, bg="yellow",width=10)
number5 = tk.Button(janela,text= 5, bg="yellow",width=10)
number6 = tk.Button(janela,text= 6, bg="yellow",width=10)
number7 = tk.Button(janela,text= 7, bg="yellow",width=10)
number8 = tk.Button(janela,text= 8, bg="yellow",width=10)
number9 = tk.Button(janela,text= 9, bg="yellow",width=10)

#operadores matemáticos
adicao = tk.Button(janela,text= "*", bg="red",width=10)
subtracao = tk.Button(janela,text= "-", bg="red",width=10)
divisao = tk.Button(janela,text= "/", bg="red",width=10)
multiplicacao = tk.Button(janela,text= "*", bg="red",width=10)

#apagar e resultado
deletar = tk.Button(janela,text= "c", bg="blue",width=10)
resultado = tk.Button(janela,text= "=", bg="blue",width=10)

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