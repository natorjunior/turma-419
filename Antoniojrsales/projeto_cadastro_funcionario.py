class Funcionario:
    def __init__(self, id, nome, sexo, cargo, ativo, salario):
        self.id = id
        self.nome = nome
        self.sexo = sexo
        self.cargo = cargo
        self.ativo = ativo
        self.salario = salario
        
    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada com sucesso")

class Funcionario_Ti(Funcionario):
    def __init__(self, id, nome, sexo, cargo, ativo, salario, linguagem_preferida):
        super().__init__(id, nome, sexo, cargo, ativo, salario)
        self.linguagem_preferida = linguagem_preferida

class Funcionario_Adm(Funcionario):
    def __init__(self, id, nome, sexo, cargo, ativo, salario, habilidade):
        super().__init__(id, nome, sexo, cargo, ativo, salario)
        self.habilidade = habilidade



pessoa1 = Funcionario_Ti(1, 'João', 'M', 'gerente', True, 10000, 'Python')

pessoa2 = Funcionario_Adm(2, 'Maria', 'M', 'supervisor', True, 5000, 'excel')

lista_de_func = [pessoa1,pessoa2]
for p in lista_de_func:
    print(p.nome)