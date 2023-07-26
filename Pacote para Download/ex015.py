# Escreva um programa que pergunte a quantidade em Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

k = float(input('Quantos Km o veículo rodou?: '))
d = int(input('Por quantos dias o veículo foi ultilizado?: '))
v = (d * 60) + (k * 0.15)
print('O valor total a pagar será de R$ {:.2f}'.format(v))


