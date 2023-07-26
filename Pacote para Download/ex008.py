#Escreva um programa que leia um número em metros e o exiba convertido em centímetros e milímetros

n = float(input('Digite um valor em metros: '))
c = n*100
m = n*1000
print('O valor em centímetros é {} e o valor em milímetros é {}'.format(c, m))
