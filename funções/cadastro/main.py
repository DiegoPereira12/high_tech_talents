# Fazer um cadastro de 3 campos e guarda-lo em 
# um dicionário (Console)
# 1-) Entender o problema
# 2-) Planejar a solução
# -Criar um menu no console com 3 opções: 
#   - Sair 
#   - Cadastrar 
#   - Listar
# 3-) Dividir/Planejar Tarefas
#   - Preparar um arquivo Python (Este aqui mesmo)
#   - Criar Loop para o menu principal
#   - Criar "Tela" Cadastrar 
#       -Perguntar campo Nome
#       -Perguntar campo Data Nascimento
#       -Perguntar campo Endereço
#   - Criar "Tela" Listar
#       -Preparar Prints Dicionario
#   - Criar Funcionalidade Sair    
# 4-) Estimar tempo de desenvolvimento (Até o final da aula)

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
        