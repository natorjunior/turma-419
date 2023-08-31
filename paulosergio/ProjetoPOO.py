
class Funcionario:
    def __init__(self, id, nome, cargo, salario):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_informações (self):
        print(f"ID:{self.id}")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salario: {self.salario}")

class FuncionarioTI(Funcionario):
    
    def __init__(self, id, nome, cargo, salario, linguagem_preferida):
        super().__init__(id, nome, cargo, salario)
        self.linguagem_preferida = linguagem_preferida

    def exibir_informações(self):
        super().exibir_informações()
        print(f"Linguagem Preferida: {self.linguagem_preferida}")
        
        
funcionario1 = Funcionario(id=1, nome="João", cargo="Analista", salario=5000.0)
funcionario2 = FuncionarioTI(id=2, nome="Maria", cargo="Desenvolvedora", salario=6000.0, linguagem_preferida="Python")
funcionario3 = Funcionario(id=3, nome="Jose", cargo="Administrativo", salario=3000.0)

funcionario1.exibir_informações()
print("\n")
funcionario2.exibir_informações()
print("\n")
funcionario3.exibir_informações()









