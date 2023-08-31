class Leao:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @property#
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self,novo_nome):
        if len(novo_nome) >= 3:
            self._nome = novo_nome
        else:
            print("O nome deve ter pelo menos 3 caracteres.")

leao= Leao("Leaozinho",20)
leao.nome = '--'
print(leao.nome)