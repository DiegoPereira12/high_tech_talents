
from transporte_terrestre.transporte_terrestre import Carro, carro1, carro2


while True:

    print('Escolha uma opção:')
    print('1 - Transporte Terrestre')
    print('2 - Transporte Aquático')
    print('3 - Transporte Áereo')
    print('4 - Sair')

    opcao = int(input('=> '))

    if opcao == 1:
        print('1 - Carro')
        print('2 - Moto')
        opcao = int(input('=> '))

        if opcao == 1:
            print('Temos as seguintes oções')
            
           
         
    elif opcao == 2:
        print('1 - Navio')
        print('2 - Lancha')
        opcao = int(input('=> '))
    
    elif opcao == 3:
        print('1 - Avião')
        print('2 - Helicoptero')
        opcao = int(input('=> '))
    
    elif opcao == 4:
        break

    else:
        print('Opção Inválida')

  