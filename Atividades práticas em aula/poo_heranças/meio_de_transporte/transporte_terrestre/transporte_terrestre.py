class MeioDeTransporte():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 
class Carro(MeioDeTransporte):
    def __init__(self, marca, modelo, combustivel):
        super().__init__(marca, modelo)
        self.combustivel = combustivel
    
    def imprime(self,marca, modelo, combustivel):
       print(f'=> Carro da {self.marca}, modelo {self.modelo}, combustível {self.combustivel}.')

class Moto(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def imprime(self,marca, modelo):
       print (f'=> Moto da {self.marca}, modelo {self.modelo}.')
