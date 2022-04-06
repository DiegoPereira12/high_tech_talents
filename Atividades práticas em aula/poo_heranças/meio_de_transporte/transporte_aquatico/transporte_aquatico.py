class MeioDeTransporte():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 
class Navio(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def imprime(self, marca, modelo):
       print(f'=> Navio {self.marca}, modelo {self.modelo}.')

class Lancha(MeioDeTransporte):
    def __init__(self, marca, modelo, tamanho):
        super().__init__(marca, modelo)
        self.tamanho = tamanho

    def imprime(self, marca, modelo, tamanho):
        print(f'=> Lancha {self.marca}, modelo {self.modelo}, tamanho {self.tamanho}.')
