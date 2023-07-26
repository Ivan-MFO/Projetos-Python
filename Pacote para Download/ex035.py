#Desenvolva um programa que leia o comprimento de três retas e digite ao usuário se elas podem ou não formar um triângulo
print('-='*15)
print('Analisador de triangulos:')
print('-='*15)

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos formam um triangulo!')
else:
    print('Os segmentos não formam um triangulo!')
