import tkinter as tk
janela = tk.Tk()

# Criando widgets
widget1 = tk.Button(janela, text="1", height=2, width=5)
widget2 = tk.Button(janela, text="2", height=2, width=5)
widget3 = tk.Button(janela, text="3", height=2, width=5)
widget4 = tk.Button(janela, text="*", height=2, width=5)
widget5 = tk.Button(janela, text="4", height=2, width=5)
widget6 = tk.Button(janela, text="5", height=2, width=5)
widget7 = tk.Button(janela, text="6", height=2, width=5)
widget8 = tk.Button(janela, text="+", height=2, width=5)
#widgetfirst = tk.Entry(janela)


widget1.grid(row=1, column=0)  # Coloca widget1 na primeira linha e primeira coluna
widget2.grid(row=1, column=1)  # Coloca widget2 na primeira linha e segunda coluna
widget3.grid(row=1, column=2)
widget4.grid(row=1, column=3)
widget5.grid(row=2, column=0)  # Coloca widget1 na primeira linha e primeira coluna
widget6.grid(row=2, column=1)  # Coloca widget2 na primeira linha e segunda coluna
widget7.grid(row=2, column=2)
widget8.grid(row=2, column=3)

#widget3.grid(row=1, column=0, padx=10, pady=5, columnspan=3 )  # Coloca widget3 na segunda linha e ocupa duas colunas

janela.mainloop()