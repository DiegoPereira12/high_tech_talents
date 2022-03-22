# Tendo como dados de entrada a altura de uma pessoa..
# Construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
# (72.7*altura) - 58

print('=' * 63)
print('O sistema irá calcular o seu peso ideal, com base na sua altura')
print('=' * 63)

altura = float(input('Digite sua altura => '))

peso = altura + (72.7*altura) - 58

print(f'Baseado em sua altura {altura:.2f} seu peso ideal é {peso:.2f}')


