class MeioDeTransporte():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 
class Aviao(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def imprime(self, marca, modelo):
       print(f'Esse aviao é da {self.marca} e o modelo é {self.modelo}')

class Helicoptero(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def imprime(self, marca, modelo):
        print(f'Esse Helicoptero é da {self.marca} e o modelo é {self.modelo}')


# Istanciando Avião

aviao1 = Aviao('Airbus','A300')
aviao2 = Aviao('Boeing','767')

print(aviao1.marca)
print(aviao1.modelo)

print(aviao2.marca)
print(aviao2.modelo)

aviao1.imprime('Airbus','A300')
aviao2.imprime('Boeing','767')

print('=' * 50)

# Instanciando Helicoptero

helicoptero1 = Helicoptero('Boeing','Chinook')
helicoptero2 = Helicoptero('Airbus','BK-117')

print(helicoptero1.marca)
print(helicoptero2.modelo)

print(helicoptero1.marca)
print(helicoptero2.modelo)

helicoptero1.imprime('Boeing','Chinook')
helicoptero2.imprime('Airbus','BK-117')