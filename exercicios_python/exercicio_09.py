# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

print('=' * 55)
print('Conversor de temperatura: De Fahrenheit Para Celsius')
print('=' * 55)

f = float(input('Digite temperatura em Graus Fahrenheit => '))

c = 5 * ((f-32) / 9)

print(f'{f} graus em Fahrenheit, é equivalante a {c:.2f} graus Celsius')

