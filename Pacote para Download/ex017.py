# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

co = float(input("Digite o valor do Cateto Oposto: "))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hi = hypot(co, ca)
print ('O valor do comprimento da hipotenusa é {:.2f}'.format(hi))

