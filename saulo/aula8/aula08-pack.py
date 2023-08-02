import tkinter as tk
janela = tk.Tk()

# Criando widgets
label1 = tk.Label(janela, text="Eu Sou", bg="red", width=10, height=1)
label2 = tk.Label(janela, text="O", bg="green", width=20, height=2)
label3 = tk.Label(janela, text="Faraó´´oóó", bg="blue", width=40, height=4)
label4 = tk.Label(janela)
# Posicionando os widgets usando pack
label1.pack()
label2.pack()
label3.pack()


janela.mainloop()