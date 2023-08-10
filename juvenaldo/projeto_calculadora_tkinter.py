import tkinter as tk

janela = tk.Tk()

def print_label (texto_do_btn):
    concatena = str_global_tela.get() + texto_do_btn
    str_global_tela.set(concatena)
    widget1.config(text=str_global_tela.get())

def deletar():
    str_global_tela.set('')
    widget1.config(text=str_global_tela.get())

def operacoes():
    widget1.config(text=eval(str_global_tela.get()))



str_global_tela = tk.StringVar()
str_global_tela.set('')

widget1 = tk.Label(janela, text="Widget 1",height=7)
btn1 = tk.Button(janela, text="1",width=10, command=lambda: print_label('1'))
btn2 = tk.Button(janela, text="2",width=10, command=lambda: print_label('2'))
btn3 = tk.Button(janela, text="3", width=10, command=lambda: print_label('3'))
btn4 = tk.Button(janela, text="-", width=10, bg = "yellow", command=lambda: print_label('-'))
widget2 = tk.Label(janela, text="Widget 1")
btn5 = tk.Button(janela, text="4",width=10, command=lambda: print_label('4'))
btn6 = tk.Button(janela, text="5",width=10, command=lambda: print_label('5'))
btn7 = tk.Button(janela, text="6", width=10, command=lambda: print_label('6'))
btn8 = tk.Button(janela, text="+", width=10, bg = "yellow", command=lambda: print_label('+'))
widget3 = tk.Label(janela, text="Widget 1")
btn9 = tk.Button(janela, text="7",width=10, command=lambda: print_label('7'))
btn10 = tk.Button(janela, text="8",width=10, command=lambda: print_label('8'))
btn11 = tk.Button(janela, text="9", width=10, command=lambda: print_label('9'))
btn12 = tk.Button(janela, text="/", width=10, bg = "yellow", command=lambda: print_label('/'))
widget4 = tk.Label(janela, text="Widget 3")
btn13 = tk.Button(janela, text="C",width=10, bg = "red", command= deletar )
btn14 = tk.Button(janela, text="0",width=10, bg = "grey", command=lambda: print_label('0'))
btn15 = tk.Button(janela, text="=", width=10, bg = "yellow", command=lambda: operacoes())
btn16 = tk.Button(janela, text="*", width=10, bg = "yellow", command=lambda: print_label('*'))

widget1.grid(row=0, column=0, columnspan=4)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=1, column=3)

btn5.grid(row=2, column=0)
btn6.grid(row=2, column=1)
btn7.grid(row=2, column=2)
btn8.grid(row=2, column=3)


btn9.grid(row=3, column=0)
btn10.grid(row=3, column=1)
btn11.grid(row=3, column=2)
btn12.grid(row=3, column=3)
btn13.grid(row=4, column=0)
btn14.grid(row=4, column=1)
btn15.grid(row=4, column=2)
btn16.grid(row=4, column=3)
tk.mainloop()