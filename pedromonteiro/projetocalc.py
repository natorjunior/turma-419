# from soma import soma
# from sub import sub
# from mult import mult
#
# print(soma(10,80))
# print(sub())
# print(mult())

from projeto1 import soma,sub,mult,div

menu = input("Qual operação voce deseja realizar?")
a = int(input("digite o numero"))
b = int(input("digite o numero"))
if menu == "soma" or menu == "+":
    print(soma(a,b))
elif menu == "sub" or menu== '-':
    print(sub(a,b))
elif menu == "mult" or menu == "*":
    print(mult(a,b))
elif menu == "div" or menu =="/":
    print(div(a,b))


