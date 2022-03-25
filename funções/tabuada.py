from os import system

def tabuada():

    print('=' * 50)
    print('Bem vindo, este sistema irá simular uma Tabuada 0 a 10')
    print('=' * 50)

    while True:

        print('Selecione uma opcao => ')
        print('1 - Multiplicar')
        print('2 - Sair')
        opcao = int(input('=> '))

        system('cls')

        if opcao == 1:
            valor = int(input('Entre com um número para saber a tabuada: '))  
            aux = 0  
            while(aux <= 10):  
                print(f'{valor} x {aux} = {valor*aux}')  
                aux = aux + 1
        
        elif opcao == 2:
            print('Fim da Tabuada')
            break
        else:
            print('Opção invalida')

tabuada()