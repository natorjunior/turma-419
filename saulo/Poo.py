class Carro ():
    def __init__(self,fabricante_carro,modelo_carro,cor_carro) -> None:
        self.fabricante = fabricante_carro
        self.modelo = modelo_carro
        self.cor = cor_carro
    
    def ligar(self):
        return "Carro ligado!"
    
    def acelerar(self):
        return "Carro acelerando."
    

    