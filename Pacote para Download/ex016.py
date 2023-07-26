#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc
real = float(input('Digite um número real qualquer: '))
print ('O valor digitado foi {} e a sua porção interira foi {}'.format(real, trunc(real)))
