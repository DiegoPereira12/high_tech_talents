# Fazer um programa que imprima a tabuada de 0 até 0 10
# no (Console)
# 1-) Entender o problema
    # Gerar as tabuadas de 0 até o 10 no console
# 2-) Planejar a solução(Console)
    # Um login de boas vindas
    # Menu
        # Multiplicar
        # Sair
# 3-) Dividir/Planejar Tarefas
    # Criação tela login
    # Criação Menu principal
    # Criação funcionalidade "Sair"
    # Criação Tela "Multiplicar"
    # Prepara loops
# 4-) Estimar tempo de desenvolvimento (Até o final da aula)

from os import system
from tkinter import E


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



