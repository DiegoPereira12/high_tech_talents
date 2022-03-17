# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

altura = float(input('Digite a altura do quadrado => '))
largura = float(input('Digite a largura do quadrado => '))

area = altura * largura
dobro = (area * 2)

print(f'Se a altura e {altura} e a largura {largura} o dobro dessa área é {dobro}')