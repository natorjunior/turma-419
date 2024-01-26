import tkinter as tk
janela = tk.Tk()
janela.title('Calculadora')


# Criando widgets
widgetfirst = tk.Label(janela, width= 5, height=5)
widget1 = tk.Button(janela, text="7", height=2, width=10)
widget2 = tk.Button(janela, text="8", height=2, width=10)
widget3 = tk.Button(janela, text="9", height=2, width=10)
widget4 = tk.Button(janela, text="*", height=2, width=10, background="red")
widget5 = tk.Button(janela, text="4", height=2, width=10)
widget6 = tk.Button(janela, text="5", height=2, width=10)
widget7 = tk.Button(janela, text="6", height=2, width=10)
widget8 = tk.Button(janela, text="+", height=2, width=10, background="red")
widget9 = tk.Button(janela, text="1", height=2, width=10)
widget10 = tk.Button(janela, text="2", height=2, width=10)
widget11 = tk.Button(janela, text="3", height=2, width=10)
widget12 = tk.Button(janela, text="-", height=2, width=10, background="red")
widget13 = tk.Button(janela, text="C", height=2, width=10, background="blue")
widget14 = tk.Button(janela, text="0", height=2, width=10)
widget15 = tk.Button(janela, text="=", height=2, width=10, background="green")
widget16 = tk.Button(janela, text="/", height=2, width=10, background="red")
#

widgetfirst.grid(row=0, column=0) 
widget1.grid(row=1, column=0)  # Coloca widget1 na primeira linha e primeira coluna
widget2.grid(row=1, column=1)  # Coloca widget2 na primeira linha e segunda coluna
widget3.grid(row=1, column=2)
widget4.grid(row=1, column=3)
widget5.grid(row=2, column=0)  # Coloca widget1 na primeira linha e primeira coluna
widget6.grid(row=2, column=1)  # Coloca widget2 na primeira linha e segunda coluna
widget7.grid(row=2, column=2)
widget8.grid(row=2, column=3)
widget9.grid(row=3, column=0)  # Coloca widget1 na primeira linha e primeira coluna
widget10.grid(row=3, column=1)  # Coloca widget2 na primeira linha e segunda coluna
widget11.grid(row=3, column=2)
widget12.grid(row=3, column=3)
widget13.grid(row=4, column=0)  # Coloca widget1 na primeira linha e primeira coluna
widget14.grid(row=4, column=1)  # Coloca widget2 na primeira linha e segunda coluna
widget15.grid(row=4, column=2)
widget16.grid(row=4, column=3)


#)  # Coloca widget3 na segunda linha e ocupa duas colunas

janela.mainloop()