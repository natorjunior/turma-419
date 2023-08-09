import tkinter as tk

janela = tk.Tk()

# Criando widgets
widget1 = tk.Label(janela, text="Widget 1")
widget2 = tk.Button(janela, text="Widget 2")
widget3 = tk.Button(janela, text="Widget 3")
widget4 = tk.Entry(janela)

widget1.grid(row=0, column=0)  # Coloca widget1 na primeira linha e primeira coluna
widget2.grid(row=0, column=1)  # Coloca widget2 na primeira linha e segunda coluna
widget3.grid(row=0, column=2)  # Coloca widget3 na primeira linha e segunda coluna
widget4.grid(row=1, column=0, columnspan=3)  # Coloca widget4 na segunda linha e ocupa duas colunas

widget1.grid(row=0, column=0, padx=10, pady=5)  # Adiciona espaçamento de 10 pixels na direção x e 5 pixels na direção y

tk.mainloop()