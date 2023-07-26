#Faça um programa que mostre na tela uma contagem regressiva para a estoura de fogos de artificio, indo de 10 a 0, com uma pausa de 1 segundo entre eles

from time import sleep

for cont in range(10, -1, -1):
        sleep(1)
        print(cont)
print('BOOOOOOM    BOOOOOOM    POOOOOW')