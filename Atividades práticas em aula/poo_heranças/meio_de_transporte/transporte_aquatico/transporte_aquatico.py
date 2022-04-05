class MeioDeTransporte():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 

class Aviao(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def imprime(self):
       print(f'Esse aviao é da {self.marca} e o modelo é {self.modelo}')

class Helicoptero(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def imprime(self):
        print(f'Esse Helicoptero é da {self.marca} e o modelo é {self.modelo}')