class Livro():
    def __init__(self):
        self.titulo = "Curso Python"
        self.autor = "Guido Van Rossum"

    def imprime(self):
        print(f'Esse livro é {self.titulo} e o Autor é {self.autor}')

# Instanciando o objeto

livro1 = Livro()
print(livro1)

# Listando os atributos

print(livro1.autor)
print(livro1.titulo)

# listando um método de uma classe

livro1.imprime()