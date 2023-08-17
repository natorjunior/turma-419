class SysInformatica():
    def __init__(self,nome_item,preco_item):
        self.item = nome_item
        self.preco = preco_item
        self.quantidade = 0

    def gerar_fatura (self):
        valor_total = self.preco * self.quantidade
        return (valor_total)

sysdom = SysInformatica("Mouse",50)
sysdom.quantidade = 10
print(sysdom.gerar_fatura())

