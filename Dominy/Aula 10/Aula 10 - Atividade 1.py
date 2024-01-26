class Carro():
    def __init__(self,fabricante_carro,modelo_carro, cor_carro) -> None:
        self.fabricante = fabricante_carro
        self.modelo = modelo_carro
        self.cor = cor_carro
    def ligar (self):
        return "Carro ligado."

    def acelerador(self):
        return "Carro acelerando."

# Dados
fabricante = "BMW"
modelo = "E36"
cor = "Azul"
meu_carro = Carro(fabricante,modelo, cor)

print(meu_carro.fabricante)
print(meu_carro.ligar())