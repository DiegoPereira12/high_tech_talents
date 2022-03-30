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

nome = input('Digite seu nome => ')
valor = float(input('Quanto você ganha por hora? R$ : '))
hora = float(input('Quantas horas você trabalhou?: '))

salario = valor * hora

print(f'O valor recebido por hora é {valor} reais, vezes {hora} horas trabalhadas, seu salário BRUTOé esse mês é R${salario} reais.')
print()