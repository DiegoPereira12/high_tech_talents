# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês
# Calcule e mostre o total do seu salário no referido mês.

print('=' * 25)
print('$$$$ Cálculo Salário $$$')
print('=' * 25)

valor = float(input('Quanto você ganha por hora? R$ : '))
hora = float(input('Quantas horas você trabalhou?: '))

salario = valor * hora

print(f'O valor recebido por hora é {valor} reais, vezes {hora} horas trabalhadas, seu salário é esse mês é R${salario} reais.')
