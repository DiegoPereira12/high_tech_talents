from time import sleep
from cadastro import cadastro, listar
from os import system

usuario = input("Entre com o seu nome: ")
print('=' * 25)
print(f"Seja Bem-vindo {usuario} !")
print('=' * 25)

lista = []

while True:

    print("Selecione uma opção:")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")

    opcao = int(input("=> "))

    if opcao == 1:
        cadastro()
        sleep(5)
        system('cls')

    elif opcao == 2: 
        listar()
            
    elif opcao == 3:
        print("Saindo do sistema...")
        break
    else:
        print(f'ATENÇÃO {usuario} opção inválida, tente novamente. \n')
        