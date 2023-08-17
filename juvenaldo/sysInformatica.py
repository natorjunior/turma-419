
class Sysinformatica:
    def __init__(self,nome_item, preco_unitario,valor_fatura) -> None:
        self.item = nome_item
        self.preco = preco_unitario
        self.quantidade = 0
        self.valor = valor_fatura

    def gerar_fatura(self):
       q = int(input("Digite a quantidade: "))
       self.quantidade = q
       return self.quantidade * self.preco

teste = Sysinformatica("frango", 12, 15)
print(f"A quantidade total é de R$ {teste.gerar_fatura()} ")
