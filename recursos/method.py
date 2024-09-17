class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

    def dirigir(self):
        print(f"O carro {self.modelo} está dirigindo")

carro1 = Carro("Sedan")
carro1.dirigir()