class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R${self.salario:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, idade, cargo, salario, setor):
        super().__init__(nome, idade, cargo, salario)
        self.setor = setor

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Setor: {self.setor}")


# Exemplo de uso
funcionario1 = Funcionario("João", 30, "Desenvolvedor", 5000.00)
gerente1 = Gerente("Maria", 40, "Gerente de Projetos", 8000.00, "TI")

print("Informações do Funcionário:")
funcionario1.exibir_informacoes()
print("\nInformações do Gerente:")
gerente1.exibir_informacoes()