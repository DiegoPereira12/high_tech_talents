
lista = []

def cadastro():

    nome = ""
    data_nasc = ""
    endereco = ""

    while nome == "":
        nome = input("Coloque o nome: ")

    while data_nasc == "":
        data_nasc = input("Coloque a data de nascimento: ")
                
    while endereco == "":
        endereco = input("Coloque o endereço: ")

        registro = {"Nome":nome, "Data_Nascimento":data_nasc, "Endereco": endereco}
        lista.append(registro)
        print("Sucesso! Cadastrado!\n")

def listar():
    for item in lista:
        print(item)

