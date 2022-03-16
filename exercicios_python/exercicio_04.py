# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

from time import sleep

print('Insira as notas solicitadas abaixo para calcularmos a média\n')

print(30 * '=')

nota1 = float(input('Digite a primeira nota => '))
nota2 = float(input('Digite a segunda nota => '))
nota3 = float(input('Digite a terceira nota => '))
nota4 = float(input('Digite a quarta nota => '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Primeira Nota {nota1}\nSegunda Nota {nota2}\nTerceira Nota {nota3}\nQuarta Nota {nota4}\n')
print(45 * '=' )
print('Aguarde estamos calculando sua média .....')
sleep(5)
print(45 * '=' )
print(f'Sua média é {media}')

