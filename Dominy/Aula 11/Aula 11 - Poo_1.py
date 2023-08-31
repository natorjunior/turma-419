class Animal:
    def __init__(self, nome,idade,altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
class Leao(Animal):
    def rugir(self):
        print(f"{self.nome} está rugindo, ele tem {self.altura} metros de altura")
class Elefante(Animal):
    def balancar_orelhas(self):
        print(f"{self.nome} está balançando as orelhas, ele tem {self.altura} metros de altura")

leao = Leao('simba',20,2)
elefante = Elefante('dumbo',10,60)

print(leao.nome)
leao.rugir()
print(elefante.nome)
elefante.balancar_orelhas()
