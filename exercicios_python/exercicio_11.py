# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A - o produto do dobro do primeiro com metade do segundo .
# B - a soma do triplo do primeiro com o terceiro.
# C - o terceiro elevado ao cubo.

from os import system


print('=' * 50)
print('O sistema ira exibir ...\n') 
print('produto do dobro do primeiro com metade do segundo\n')
print('A soma do triplo do primeiro com o terceiro\n')
print('O terceiro elevado ao cubo')
print('=' * 50)


inteiro_1 = int(input('Digite o primeiro numero inteiro => '))
inteiro_2 = int(input('Digite o segundo numero inteiro => '))
real_1 = float(input('Digite um numero real => '))


A = 2 * inteiro_1 * inteiro_2 / 2
B = 3 * inteiro_1 + real_1
C = real_1 ** 3

print('=' * 50)
print(f'produto do dobro do primeiro com metade do segundo {A} \nA soma do triplo do primeiro com o terceiro {B} \nO terceiro elevado ao cubo {C}')
print('=' * 50)