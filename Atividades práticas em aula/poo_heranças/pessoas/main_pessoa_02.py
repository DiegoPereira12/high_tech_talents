class Pessoa():
    def __init__(self, nome, documento, localidade):
      self.nome = nome
      self.documento = documento
      self.localidade = localidade

    def dar_entrada(self):
        print("Entrando")

    def alugar(self):
        print("Alugando")



class PessoaJuridica(Pessoa):
    def __init__(self, nome, documento, localidade, data_fundacao):
        super().__init__(nome, documento, localidade)
        self.data_fundacao = data_fundacao
        
    def fundar(self):
        print("Fundando")



class PessoaFisica(Pessoa):
    def __init__(self, nome, documento, localidade, data_nascimento):
        super().__init__(nome, documento, localidade)
        self.data_nascimento = data_nascimento

    def nascer(self):
        print("Nascendo")
        self.__metodo()
    
    def __metodo(self):
        print("metodo")


pf = PessoaFisica(nome="Jeff", documento="123123", localidade="RJ", data_nascimento="01/01/2001")
pf.nascer()
pf.dar_entrada()
pf.alugar()
print(f"Documento da pessoa: {pf.documento} ")

pj = PessoaJuridica("Jeff Company", "1233123/0002-4", "RJ", "01/01/2000")
pj.fundar()
pj.dar_entrada()
pj.alugar()
print(f"Documento da empresa: {pj.documento} ")