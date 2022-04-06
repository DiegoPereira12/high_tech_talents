
from transporte_terrestre.transporte_terrestre import Carro, Moto


def main():

    while True:

        print('Escolha uma opção:')
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
                print('Temos as seguintes oções')
            
           
         
        elif opcao == '2':
            print('1 - Navio')
            print('2 - Lancha')
            opcao = input('=> ')
            if opcao == '1':
                from transporte_aquatico.transporte_aquatico import Navio
                navio = Navio = Navio(marca='', modelo='')

            elif opcao == '2':
                pass
               
           
    
        elif opcao == '3':
            print('1 - Avião')
            print('2 - Helicoptero')
            opcao = input('=> ')
    
        elif opcao == '4':
            break

        else:
            print('Opção Inválida')

if __name__ == '__main__':
    main()
  