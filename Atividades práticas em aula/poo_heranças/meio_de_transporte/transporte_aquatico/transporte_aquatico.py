class MeioDeTransporte():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 

class Navio(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def imprime(self, marca, modelo):
       print(f'Esse Navio é {self.marca} e o modelo é {self.modelo}')

class Lancha(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def imprime(self, marca, modelo):
        print(f'Essa Lancha é da {self.marca} e o modelo é {self.modelo}')

# Instanciando Avião

navio1 = Navio('Harland and Wolff,','Titanic')
navio2 = Navio('Pirata','JackSparrow')

print(navio1.marca)
print(navio1.modelo)

print(navio2.marca)
print(navio2.modelo)

navio1.imprime('Airbus','A300')
navio2.imprime('Boeing','767')

print('=' * 50)

# Instanciando Lanchas

lancha1 = Lancha('Azimut Yachts','Azimut 62')
lancha2 = Lancha('Schaefer Yachts','schaefer-660')

print(lancha1.marca)
print(lancha1.modelo)

print(lancha2.marca)
print(lancha2.modelo)

lancha1.imprime('Airbus','A300')
lancha2.imprime('Boeing','767')