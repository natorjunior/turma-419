import tkinter as tk

def print_label(texto_do_btn):
    concatena = str_global_tela.get()+texto_do_btn
    str_global_tela.set(concatena)
    widgetEntrada.config(text=str_global_tela.get())

def limpar():
    str_global_tela.set('')
    widgetEntrada.config(text=str_global_tela.get())

def operacoes():
    resultado = eval(str_global_tela.get())
    str_global_tela.set(resultado)
    widgetEntrada.config(text=str_global_tela.get())

janela = tk.Tk()

str_global_tela = tk.StringVar()
str_global_tela.set('')

# Criando botões
widgetEntrada = tk.Label(janela, height=5, font= ('Helvetica', 22))
widget0 = tk.Button(janela, text="0", width=6, height=3, bg= 'yellow', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label('0'))
widget1 = tk.Button(janela, text="1", width=6, height=3, bg= 'yellow', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label('1'))
widget2 = tk.Button(janela, text="2", width=6, height=3, bg= 'yellow', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label('2'))
widget3 = tk.Button(janela, text="3", width=6, height=3, bg= 'yellow', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label('3'))
widget4 = tk.Button(janela, text="4", width=6, height=3, bg= 'yellow', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label('4'))
widget5 = tk.Button(janela, text="5", width=6, height=3, bg= 'yellow', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label('5'))
widget6 = tk.Button(janela, text="6", width=6, height=3, bg= 'yellow', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label('6'))
widget7 = tk.Button(janela, text="7", width=6, height=3, bg= 'yellow', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label('7'))
widget8 = tk.Button(janela, text="8", width=6, height=3, bg= 'yellow', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label('8'))
widget9 = tk.Button(janela, text="9", width=6, height=3, bg= 'yellow', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label('9'))
widgetC = tk.Button(janela, text="C", width=6, height=3, bg= 'green', fg= 'black', font= ('Helvetica', 16), command=limpar)
widgetIgual = tk.Button(janela, text="=", width=6, height=3, bg= 'red', fg= 'black', font= ('Helvetica', 16), command=operacoes)
widgetDiminuir = tk.Button(janela, text="-", width=6, height=3, bg= 'brown', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label(' - '))
widgetSomar = tk.Button(janela, text="+", width=6, height=3, bg= 'brown', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label(' + '))
widgetMultiplicar = tk.Button(janela, text="*", width=6, height=3, bg= 'brown', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label(' * '))
widgetDividir = tk.Button(janela, text="/", width=6, height=3, bg= 'brown', fg= 'black', font= ('Helvetica', 16), command=lambda:print_label(' / '))


widgetEntrada.grid(row=0, column=0, columnspan=4)
widget0.grid(row=4, column=1)  
widget1.grid(row=3, column=0)  
widget2.grid(row=3, column=1)  
widget3.grid(row=3, column=2)  
widget4.grid(row=2, column=0)
widget5.grid(row=2, column=1)
widget6.grid(row=2, column=2)
widget7.grid(row=1, column=0)
widget8.grid(row=1, column=1)
widget9.grid(row=1, column=2)
widgetC.grid(row=4, column=0)
widgetIgual.grid(row=4, column=2)
widgetDiminuir.grid(row=2, column=3)
widgetSomar.grid(row=3, column=3)
widgetMultiplicar.grid(row=4, column=3)
widgetDividir.grid(row=1, column=3)
#widget1.grid(row=0, column=0, padx=10, pady=5)  # Adiciona espaçamento de 10 pixels na direção x e 5 pixels na direção y


tk.mainloop()