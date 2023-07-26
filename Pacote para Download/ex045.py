#Crie um programa que faça o computador jogar jokenpol com você:

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('{:=^40}'.format(' BEM VINDO AO GAME JOKEMPOL!!! '))
print('''Suas opcções de escolha são:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua opção de escolha? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('POL!!!')
sleep(0.5)
print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0: #PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Inválida!')
elif computador == 1: #PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada Inválida!')
elif computador == 2: #TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida!')
