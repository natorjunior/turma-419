class Funcionario:
    def __init__(self, ID,nome,cargo,salario,formacao):
        self.ID = ID
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.formacao = formacao
    def exibir_informacoes_funcionario(self):
        return(f"Nome: {self.nome}\nCargo: {self.cargo}\nSalário: R${self.salario}")


class FuncionarioTI(Funcionario):
    def __init__(self,ID,nome,cargo,salario,formacao,linguagem_preferida):
        super().__init__(ID,nome,cargo,salario,formacao)
        self.linguagem_preferida = linguagem_preferida


    def exibir_informacoes_funcionario(self):
        informacoes_ti = super().exibir_informacoes_funcionario()
        return f"{informacoes_ti}\nLinguagem Preferida: {self.linguagem_preferida}"

class FuncionarioADM(Funcionario):
    def __init__(self,ID,nome,cargo,salario,formacao,funcao):
        super().__init__(ID, nome, cargo, salario,formacao)
        self.funcao = funcao

    def exibir_informacoes_funcionario(self):
        informacoes_adm = super().exibir_informacoes_funcionario()
        return f"{informacoes_adm}\nAtua na função: {self.funcao}"


funcionario1 = FuncionarioTI(1,"Dominy Martins Mesquita","Cientista de Dados", 4500.00,"Data Science","Python")
funcionario2 = FuncionarioADM(2, "Alan Jesse do Nascimento Luz","Professor", 7000.00,"Teologia","Gestão de Documentos")
print(funcionario1.exibir_informacoes_funcionario())
print("----------------------------------------------")
print(funcionario2.exibir_informacoes_funcionario())




