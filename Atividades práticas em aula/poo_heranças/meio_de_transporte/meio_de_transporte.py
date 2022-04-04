class MeioDeTransporte():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
 

class TransporteTerreste(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def carro(self):
        pass

    def moto(self):
        pass

class TransporteAquatico(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def barco(self):
        pass

    def lancha(self):
        pass

class TransporteAreo(MeioDeTransporte):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def aviao(self):
        pass

    def helicoptero(self):
        pass