# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print('Conversor de temperatura: De Celsius Para Fahrenheit ')

print('=' * 55)

c = float(input('Digite temperatura em Graus Fahrenheit => '))

f = (9*c/5 + 32)

print(f'{c} graus em Celsius , é equivalante a {f:.2f} graus Fahrenheit')

