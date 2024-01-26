class Funcionario:
    def __init__(self, ID, nome, salario, cargo):
        self.ID = ID
        self.nome = nome
        self.salario = salario
        self.cargo = cargo


class Funcionario_Suporte(Funcionario):
    def __init__(self, ID, nome, salario, cargo,time,nivel):
        super().__init__(ID, nome, salario, cargo)
        self.time = time
        self.nivel = nivel
    def descricao_Suporte (self):
        return f"{self.nome} prefere {self.time}"
    
class Funcionario_TI(Funcionario):
    def __init__(self, ID, nome, salario, cargo, linguagem):
        super().__init__(ID, nome, salario, cargo)
        self.linguagem = linguagem
        
    def descricao_TI(self):
        return f"{self.nome} utiliza da linguagem {self.linguagem}"

class Funcionario_Analista(Funcionario):
    def __init__(self, ID, nome, salario, cargo, especializacao):
        super().__init__(ID, nome, salario, cargo)
        self.especializacao = especializacao

    def descricao_Analista(self):
        return f"\f{self.nome} é Analista de {self.especializacao}\f"
    
    def aumento(self):
        return f'Possível ajuste salarial de 10% (Aumento de R$ {self.salario * 0.10:.2f}). \fTotalizando R$ {self.salario * 0.10 + self.salario:.2f}'



funcionario_analista = Funcionario_Analista (1,"Adalberto",20000,"Analista de Dados","Mercado")
print(funcionario_analista.descricao_Analista())
print(funcionario_analista.aumento())