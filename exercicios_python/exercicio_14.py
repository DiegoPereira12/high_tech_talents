'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
'''

print('=' * 50)
print('Peixaria Tio João - Calcular peso do Peixe')
print('ATENCÃO!!! Não exceder 50 quilos, sujeito cobrança de multa ')
print('=' * 50)

excesso = 0
multa = 0

peso = float(input('Quantos quilos de Peixe você pescou? '))

if peso <= 50:
    print(f'Você pescou {peso} quilo(s), esta dentro das normas permitidas.')

elif peso >= 51:
    excesso = peso - 50
    multa = excesso * 4
    print(f'Você pescou {peso} quilo(s), referente ao excesso {excesso} quilo(s), você pagara uma multa de R$ {multa} reais')
	