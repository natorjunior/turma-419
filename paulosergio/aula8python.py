# import tkinter as tk
# print ("Bem vindo a Calculadora Stephane Maria!")
# while True:
#     print("Selecione a operação:")
#     print("1. Soma")
#     print("2. Subtração")
#     print("3. Multiplicação")
#     print("4. Divisão")
#     print("5. Porcentagem")
#     print("6. Exponenciação")
#     print("0. Sair")
#     choice = input ("Digite o número que deseja calcular: ")
#     if choice == "0":
#         print("   ")
#         print("Calculadora encerrada.")
#         break
#     a = float(input("Digite o primeiro número: "))
#     b = float(input("Digite o segundo número: "))
#     if choice == "1":
#         result = somar(a, b)
#         print("Resultado: ", result)
#     elif choice == "2":
#         result = subtrair(a, b)
#         print("Resultado: ", result)
#     elif choice == "3":
#         result = multiplicar(a, b)
#         print("Resultado: ", result)
#     elif choice == "4":
#         result = dividir(a, b)
#         print("Resultado: ", result)
#     elif choice == "5":
#         result = porcentagem(a, b)
#         print("Resultado: ", result)
#     elif choice == "6":
#         result = exponenciacao(a, b)
#         print("Resultado: ", result)
#     else:
#        print("Opção inválida. Por favor, escolha uma operação válida.")

# janela = tk.Tk()
# janela.title("Calculadora")
# janela.geometry("300x200")


#Primeiro exercício
# import tkinter as tk

# janela = tk.Tk()
# janela.title("Janela de Entrada")
# janela.geometry("300x200")
# # Criando widgets
# widget1 = tk.Label(janela, text="Calculadora")
# widget2 = tk.Button(janela, text="Resposta")
# widget3 = tk.Entry(janela)
# widget1.grid(row=0, column=1)  # Coloca widget1 na primeira linha e primeira coluna
# widget2.grid(row=2, column=1)  # Coloca widget2 na primeira linha e segunda coluna
# widget3.grid(row=1, column=0, columnspan=3)  # Coloca widget3 na segunda linha e ocupa duas colunas
# tk.mainloop()


# Segundo exercício calculadora
import tkinter as tk

def nota (texto):
    concatena = numero.get()+ str(texto)
    numero.set(concatena)
    widget18.config(text=numero.get())

def calcular ():
    expressao = numero.get()
    try:
        resultado = eval(expressao)
        numero.set(resultado)
    except:
        numero.set("ERRO")
    widget18.config(text=numero.get())

def deletar ():
    widget18.config(text="")
    numero.set("")
    
  
janela = tk.Tk()
janela.title("Calculadora")
numero = tk.StringVar()
numero.set("")

widget1 = tk.Label(janela, text="Calculadora")
widget2 = tk.Button(janela, text="1", width=20, height=2, bg="blue", command=lambda x=1:nota(x))
widget3 = tk.Button(janela, text="2", width=20, height=2, bg="blue", command=lambda x=2:nota(x))
widget4 = tk.Button(janela, text="3", width=20, height=2, bg="blue", command=lambda x=3:nota(x))
widget5 = tk.Button(janela, text="+", width=20, height=2, bg="green", command=lambda x="+":nota(x))
widget6 = tk.Button(janela, text="4", width=20, height=2, bg="blue", command=lambda x=4:nota(x))
widget7 = tk.Button(janela, text="5", width=20, height=2, bg="blue", command=lambda x=5:nota(x))
widget8 = tk.Button(janela, text="6", width=20, height=2, bg="blue", command=lambda x=6:nota(x))
widget9 = tk.Button(janela, text="-", width=20, height=2, bg="red", command=lambda x="-":nota(x))
widget10 = tk.Button(janela, text="7", width=20, height=2, bg="blue", command=lambda x=7:nota(x))
widget11 = tk.Button(janela, text="8", width=20, height=2, bg="blue", command=lambda x=8:nota(x))
widget12 = tk.Button(janela, text="9", width=20, height=2, bg="blue", command=lambda x=9:nota(x))
widget13 = tk.Button(janela, text="*", width=20, height=2, bg="green", command=lambda x="*":nota(x))
widget14 = tk.Button(janela, text="0", width=20, height=2, bg="blue", command=lambda x=0:nota(x))                                                        
widget15 = tk.Button(janela, text="=", width=20, height=2, bg="green", command=calcular)
widget16 = tk.Button(janela, text="Del", width=20, height=2, bg="red", command=deletar)
widget17 = tk.Button(janela, text="/", width=20, height=2, bg="red", command=lambda x="/":nota(x))
widget18 = tk.Label(janela, text="",width=80, height=7)
widget1.grid(row=0, column=1)  
widget2.grid(row=4, column=0) 
widget3.grid(row=4, column=1)
widget4.grid(row=4, column=2) 
widget5.grid(row=4, column=3) 
widget6.grid(row=5, column=0) 
widget7.grid(row=5, column=1) 
widget8.grid(row=5, column=2) 
widget9.grid(row=5, column=3)
widget10.grid(row=6, column=0) 
widget11.grid(row=6, column=1) 
widget12.grid(row=6, column=2)
widget13.grid(row=6, column=3)
widget14.grid(row=7, column=1)
widget15.grid(row=7, column=2)
widget16.grid(row=7, column=0)
widget17.grid(row=7, column=3)
widget18.grid(row=1, column=0, columnspan=4)

tk.mainloop()


