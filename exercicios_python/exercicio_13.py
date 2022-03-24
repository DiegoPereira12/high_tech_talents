# Tendo como dado de entrada a altura (h) de uma pessoa
# Construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7


print('=' * 63)
print('O sistema irá calcular o seu peso ideal, com base na sua altura')
print('=' * 63)

sexo = input('Digite seu sexo (m / f) => ')
altura = float(input('Digite sua altura => '))

if sexo == 'm':
    peso = altura + (72.7*altura) - 58
    print(f'Baseado em sua altura {altura:.2f} seu peso ideal é {peso:.2f}')

elif sexo == 'f':
    peso = altura + (62.1*altura) - 44.7
    print(f'Baseado em sua altura {altura:.2f} seu peso ideal é {peso:.2f}')

else:
    print('Entrada inválida.')
