import tkinter as tk

janela = tk.Tk()
janela.title("aula_08_tkinter")
janela.geometry("500x400")

# Criando widgets
widget1 = tk.Label(janela, text="Widget 1")
widget2 = tk.Button(janela, text="Widget 2")
widget3 = tk.Entry(janela)

widget1.grid(row=0, column=0)  
widget2.grid(row=0, column=1)  
widget3.grid(row=1, column=0, columnspan=2)  

widget1.grid(row=0, column=1, padx=10, pady=5) 
widget1.grid(row=0, column=2, padx=10, pady=5) 

tk.mainloop()