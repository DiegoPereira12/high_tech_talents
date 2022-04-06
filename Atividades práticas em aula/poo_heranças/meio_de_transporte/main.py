from os import system
from time import sleep
from transporte_terrestre.transporte_terrestre import Carro, Moto
from transporte_aquatico.transporte_aquatico import Navio, Lancha
from transporte_aereo.transporte_aereo import Aviao, Helicoptero

def main():

    while True:

        print('=' * 27)
        print('Sistema Meios de Transporte')
        print('=' * 27)
        print('1 - Transporte Terrestre')
        print('2 - Transporte Aquático')
        print('3 - Transporte Áereo')
        print('4 - Sair')

        opcao = input('=> ')

        if opcao == '1':
            print('1 - Carro')
            print('2 - Moto')
            opcao = input('=> ')

            if opcao == '1':
                system('cls')
                carro1 = Carro('Chevrolet','Onix','Gasolina')
                carro2 = Carro('Ford','Ranger','Diesel')

                print('Temos os carros abaixo disponíveis:')
                carro1.imprime('Chevrolet','Chevete','Gasolina')
                carro2.imprime('Ford','Ranger','Diesel')
                sleep(5)
               
            elif opcao == '2':
                system('cls')
                moto1 = Moto('Kawasaki','Ninja1000c')
                moto2 = Moto('Honda','Hornet')

                print('Temos as Motos abaixo disponíveis:')
                moto1.imprime('Kawasaki','Ninja1000c')
                moto2.imprime('Honda','Hornet')
                sleep(5)

            else:
                system('cls')
                print('Opção Inválida')
               
        elif opcao == '2':
            print('1 - Navio')
            print('2 - Lancha')
            opcao = input('=> ')

            if opcao == '1':
                system('cls')
                navio1 = Navio('Harland and Wolff','Titanic')
                navio2 = Navio('Pirata','JackSparrow')

                print('Temos os Navios abaixo disponíveis:')
                navio1.imprime('Airbus','A300')
                navio2.imprime('Boeing','767')
                sleep(5)

            elif opcao == '2':
                system('cls')
                lancha1 = Lancha('Azimut Yachts','Azimut 62','16 pés')
                lancha2 = Lancha('Schaefer Yachts','schaefer-660','26 pés')

                print('Temos as Lanchas abaixo disponíveis:')
                lancha1.imprime('Azimut Yachts','Azimut 62','16 pés')
                lancha2.imprime('Schaefer Yachts','schaefer-660','23 pés')
                sleep(5)

            else:
                system('cls')
                print('Opção Inválida')
           
        elif opcao == '3':
            print('1 - Avião')
            print('2 - Helicoptero')
            opcao = input('=> ')

            if opcao == '1':
                system('cls')
                aviao1 = Aviao('Airbus','A300')
                aviao2 = Aviao('Boeing','767')

                print('Temos os os Aviões abaixo disponíveis:')    
                aviao1.imprime('Airbus','A300')
                aviao2.imprime('Boeing','767')
                sleep(5)
            
            elif opcao == '2':
                system('cls')
                helicoptero1 = Helicoptero('Boeing','Chinook','35 pessoas')
                helicoptero2 = Helicoptero('Airbus','BK-117','11 pessoas')

                print('Temos os Helicópteros abaixo disponíveis:')    
                helicoptero1.imprime('Boeing','Chinook','35 pessoas')
                helicoptero2.imprime('Airbus','BK-117','11 pessoas')
                sleep(5)
            
            else:
                system('cls')
                print('Opção Inválida')
    
        elif opcao == '4':
            print('Fim do sistema!!!')
            break

        else:
            system('cls')
            print('Opção Inválida')

if __name__ == '__main__':
    main()
  