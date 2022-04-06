class MeioDeTransporte():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 
class Aviao(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def imprime(self, marca, modelo):
       print(f'=> Aviao {self.marca}, modelo {self.modelo}.')

class Helicoptero(MeioDeTransporte):
    def __init__(self, marca, modelo, capacidade):
        super().__init__(marca, modelo)
        self.capacidade = capacidade

    def imprime(self, marca, modelo, capacidade):
        print(f'=> Helicoptero {self.marca}, modelo {self.modelo}, capacidade {self.capacidade}.')