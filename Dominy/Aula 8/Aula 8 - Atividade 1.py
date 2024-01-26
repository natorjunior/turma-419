import tkinter as tk

janela = tk.Tk()

#criando widgets
widget1 = tk.Label(janela, text = "Dom 1")
widget2 = tk.Button(janela, text = "Dom 2")
widget3 = tk.Entry(janela)

widget1.pack()
widget2.pack()
widget3.pack()

janela.mainloop()