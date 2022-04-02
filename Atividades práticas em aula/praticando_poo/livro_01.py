class Livro1():
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    
    def imprime(self, titulo,autor):
        print(f'Esse livro é {self.titulo} e o autor é {self.autor}')

# Criando objeto instanciando o Objeto

livro2 = Livro1('Aprendendo Excel','Pereira Costa')

# Monstrando atributos do Objeto

print(livro2.autor)
print(livro2.titulo)

livro2.imprime('Apredendo Excel','Pereira Costa')
