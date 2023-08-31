class Animal:
   def __init__(self, nome, idade):
       self.nome = nome
       self.idade = idade
   def descricao(self):
       return f"Um animal chamado {self.nome}, com {self.idade} anos."

class Leao(Animal):
   def descricao(self):
       descricao_pai = super().descricao()
       return f"Um leão chamado {self.nome}, com {self.idade} anos. {descricao_pai}"
# Usando as classes
leao = Leao("Simba", 5)
print(leao.descricao())
