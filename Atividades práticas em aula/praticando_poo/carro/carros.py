class Carros():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def imprime (self, marca, modelo):
        print(f'Esse carro é da {self.marca} e o modelo é {self.modelo}')