class Funcionario:
    def __init__(self, id, nome, cargo, salario):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    def exibir_informacoes_gerais(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R${self.salario:.2f}")
class FuncionarioTI(Funcionario):
    def __init__(self, id, nome, cargo, salario, linguagem_preferida):
        super().__init__(id, nome, cargo, salario)
        self.linguagem_preferida = linguagem_preferida

    def exibir_informacoes_gerais(self):
        super().exibir_informacoes_gerais()
        print(f"Linguagem Preferida: {self.linguagem_preferida}")

class Administracao(Funcionario):
    def __init__(self, id, nome, cargo, salario, habilidades):
        super().__init__( id, nome, cargo, salario)
        self.habilidades = habilidades
    def exibir_informacoes_gerais(self):
        super().exibir_informacoes_gerais()
        print(f"Habilidade: {self.habilidades}")


funcionario1 = FuncionarioTI(1, "Pedro", "Cientista de Dados", 20000, "Python")
funcionario2 = FuncionarioTI(2, "João", "Desenvolvedor WEB", 20000, "PHP")
funcionario3 = Administracao(3, "Jose", "Administracao", 1000, "Excel")

listadefuncionarios = [funcionario1,funcionario2,funcionario3]
for f in listadefuncionarios:
    f.exibir_informacoes_gerais()