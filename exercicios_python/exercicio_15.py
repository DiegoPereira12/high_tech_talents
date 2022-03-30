# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados... 
# 11% para o Imposto de Renda, 
# 8% para o INSS 
# 5% para o sindicato, 
# Faça um programa que nos dê:
# salário bruto
# Quanto pagou ao INSS
# Quanto pagou ao sindicato
# Salário líquido

from time import sleep

print('=' * 33)
print('Olá, vamos calcular o seu salário')
print('=' * 33)

nome_funcionario = input('Digite seu nome => ')
valor = float(input('Quanto você ganha por hora? R$ : '))
horas_trabalhadas = float(input('Quantas horas você trabalhou?: '))

salario_bruto = valor * horas_trabalhadas

print('=' * 111)
print(f'O valor recebido por hora é {valor} reais, vezes {horas_trabalhadas} horas trabalhadas, seu salário BRUTO esse mês é R$ {salario_bruto} reais.')
print('=' * 111)

print('Aguarde enquanto calculamos os descontos ...\n')
sleep(5)

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

print(f'Seu salario BRUTO é de {salario_bruto} reais, menos 11% de desconto do Imposto de Renda é {salario_bruto - ir} reais')
sleep(5)
print(f'Seu salario BRUTO é de {salario_bruto} reais, menos 8% de desconto do INSS é {salario_bruto - inss} reais')
sleep(5)
print(f'Seu salario BRUTO é de {salario_bruto} reais, menos 5% de desconto do Sindicato é {salario_bruto - sindicato} reais\n')

total_descontos = ir + inss + sindicato

print(f'Total de descontos é igual {total_descontos} reais\n')

salario_liquido = salario_bruto - ir - inss - sindicato

print('=' * 48)
print(f'{nome_funcionario} seu Salário Líquido nesse mês é {salario_liquido} reais.')
print('=' * 48)