class MeioDeTransporte():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 
class Carro(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def imprime(self,marca, modelo):
       return(f'Esse carro é da {self.marca} e o modelo é {self.modelo}')

class Moto(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def imprime(self,marca, modelo):
       return (f'Esse moto é da {self.marca} e o modelo é {self.modelo}')

# Instanciando Carro

carro1 = Carro('Chevrolet','Onix')
carro2 = Carro('Ford','Ranger')

carro1.imprime('Chevrolet','Chevete')
carro2.imprime('Ford','Ranger')

print('=' * 50)

# Instanciando Moto

moto1 = Moto('Kawasaki','Ninja1000c')
moto2 = Moto('Honda','Hornet')

moto1.imprime('Kawasaki','Ninja1000c')
moto2.imprime('Honda','Hornet')

