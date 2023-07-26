#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente deste angulo

from math import sin, cos, tan, radians

a = float(input('Digite o valor do ângulo: '))
seno = sin(radians(a))
print ('Para o angulo de {} o valor do Seno é de {:.2f}'.format(a, seno))
coss = cos(radians(a))
print ('Para o angulo de {} o valor do Cosseno é de {:.2f}'.format(a, coss))
tang = tan(radians(a))
print ('Para o angulo de {} o valor da Tangente é de {:.2f}'.format(a, tang))
