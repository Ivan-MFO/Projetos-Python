#Refaça o desafio 35 dos triângulos acrescentando o recurso de mostrar qual tipo de triângulo será formado: equilátero: todos os lados iguais, isóceles: dois lados iguais, escaleno: todos os lados diferentes

r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos podem formar um triangulo!')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos não formam um triangulo!')