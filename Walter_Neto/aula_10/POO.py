# class Carro():
#     def __init__(self, fabricante_carro, cor_carro, modelo_carro ) -> None:
#         self.fabricante = fabricante_carro
#         self.cor = cor_carro
#         self.modelo = modelo_carro
#         self.ligado = False

#     def ligar(self):
#         self.ligado = True
#         return 'Carro Ligado'

# instanciaCarro1 = Carro('algo','vermelho', 'Algo')
# print(instanciaCarro1.ligar())
# print(instanciaCarro1.cor)



class SysInformatica():
    def __init__(self,item_descricao, item_valor, item_vendido) -> None:
        self.descricao = item_descricao
        self.valor = item_valor
        self.vendido = item_vendido
        self.fatura = 0

    def Gerarfatura (self):
        self.fatura = self.valor * self.vendido
        return f'Valor faturado de {self.fatura}'


produto = str(input('Produto: '))
preco = int(input('Valor: '))
quantidade = int(input('Quantidade: '))

fome = SysInformatica(produto,preco,quantidade)
print(fome.vendido)
print(fome.Gerarfatura())
