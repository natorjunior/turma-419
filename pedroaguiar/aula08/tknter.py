import tkinter as tk

janela = tk.Tk()


widget0 = tk.Label(janela, text="", bg="silver",height=7,width=40)
widget1 = tk.Button(janela, text="1", bg="yellow",width=10)
widget2 = tk.Button(janela, text="2", bg="yellow",width=10)
widget3 = tk.Button(janela, text="3", bg="yellow",width=10)
widget4 = tk.Button(janela, text="4", bg="yellow",width=10)
widget5 = tk.Button(janela, text="5", bg="yellow",width=10)
widget6 = tk.Button(janela, text="6", bg="yellow",width=10)
widget7 = tk.Button(janela, text="7", bg="yellow",width=10)
widget8 = tk.Button(janela, text="8", bg="yellow",width=10)
widget9 = tk.Button(janela, text="9", bg="yellow",width=10)
widget10 = tk.Button(janela, text="-", bg="red",width=10)
widget11 = tk.Button(janela, text="+", bg="red",width=10)
widget12 = tk.Button(janela, text="/", bg="red",width=10)
widget13 = tk.Button(janela, text="=", bg="red",width=10)





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



janela.mainloop()