import tkinter as tk
global acumula
acumula = ''
def calcula_(text):
    global acumula
    acumula = acumula+str(text)
    widget0.config(text=acumula)
def limpar():
    global acumula
    acumula = ""
    widget0.config(text=acumula)

janela = tk.Tk()


widget0 = tk.Label(janela, text="", bg="silver",height=7,width=40)
widget1 = tk.Button(janela, text="1", bg="yellow",width=10,command=lambda x=1: calcula_(x))
widget2 = tk.Button(janela, text="2", bg="yellow",width=10,command=lambda x=2: calcula_(x))
widget3 = tk.Button(janela, text="3", bg="yellow",width=10,command=lambda x=3: calcula_(x))
widget4 = tk.Button(janela, text="4", bg="yellow",width=10,command=lambda x=4: calcula_(x))
widget5 = tk.Button(janela, text="5", bg="yellow",width=10,command=lambda x=5: calcula_(x))
widget6 = tk.Button(janela, text="6", bg="yellow",width=10,command=lambda x=6: calcula_(x))
widget7 = tk.Button(janela, text="7", bg="yellow",width=10,command=lambda x=7: calcula_(x))
widget8 = tk.Button(janela, text="8", bg="yellow",width=10,command=lambda x=8: calcula_(x))
widget9 = tk.Button(janela, text="9", bg="yellow",width=10,command=lambda x=9: calcula_(x))
widget10 = tk.Button(janela, text="-", bg="red",width=10)
widget11 = tk.Button(janela, text="+", bg="red",width=10)
widget12 = tk.Button(janela, text="/", bg="red",width=10)
widget13 = tk.Button(janela, text="x", bg="red",width=10)
widget14 = tk.Button(janela, text="C", bg="green",width=10, command=limpar)
widget15 = tk.Button(janela, text="0", bg="yellow",width=10,command=lambda x=0: calcula_(x))
widget16 = tk.Button(janela, text="=", bg="red",width=10)







widget0.grid(row=0, column=0,columnspan=5)
widget1.grid(row=1, column=0)
widget2.grid(row=1, column=1)
widget3.grid(row=1, column=2)
widget4.grid(row=2, column=0)
widget5.grid(row=2, column=1)
widget6.grid(row=2, column=2)
widget7.grid(row=3, column=0)
widget8.grid(row=3, column=1)
widget9.grid(row=3, column=2)
widget10.grid(row=1, column=3)
widget11.grid(row=2, column=3)
widget12.grid(row=3, column=3)
widget13.grid(row=4,column=3)
widget14.grid(row=4,column=0)
widget15.grid(row=4,column=1)
widget16.grid(row=4,column=2)


janela.mainloop()