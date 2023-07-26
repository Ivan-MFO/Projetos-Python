#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados

a = float(input('Digite a altura da sua parede em metros: '))
l = float(input('Digite a largura da sua parede em metros: '))
ar = a*l
t = ar/2
print('Sua área total a ser pintada é: {}m2 e a quantidade de tinta necessária sera de {}l'.format(ar, t))
