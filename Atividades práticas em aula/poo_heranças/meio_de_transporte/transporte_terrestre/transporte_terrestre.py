class MeioDeTransporte():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 
class Carro(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def imprime(self,marca, modelo):
       print(f'Esse carro é da {self.marca} e o modelo é {self.modelo}')

class Moto(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def imprime(self,marca, modelo):
       print(f'Esse moto é da {self.marca} e o modelo é {self.modelo}')

# Instanciando Carro

carro1 = Carro('Chevrolet','Onix')
carro2 = Carro('Ford','Ranger')

print(carro1.marca)
print(carro1.modelo)

print(carro2.marca)
print(carro2.modelo)

carro1.imprime('Chevrolet','Chevete')
carro2.imprime('Ford','Ranger')

print('=' * 50)
# Instanciando Moto

moto1 = Moto('Kawasaki','Ninja1000c')
moto2 = Moto('Honda','Hornet')

print(moto1.marca)
print(moto1.modelo)

print(moto2.marca)
print(moto2.modelo)

moto1.imprime('Kawasaki','Ninja1000c')
moto2.imprime('Honda','Hornet')

