#Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando o jogador perder mostrando o total de vit[orias consecutivas que ele conquistou no final do jogo
from random import randint

print(' ********** JOGO DO PAR OU ÍMPAR ********** ')
print('Digite P para par e I para Ímpar')
cont = 0
win = 0

while True:
    jogador = ' '
    while jogador not in 'PpIi':
        jogador = str(input('Qual será sua escolha? [P/I]: ')). strip().upper()[0]
    num = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = num + computador
    print(f'Você jogou {num} e o computador jogou {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if jogador == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            win += 1
        else:
            print('Você perdeu!')
            break
    elif jogador == "I":
        if total % 2 == 1:
            print('Você ganhou!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente... ')
print(f'FIM DE JOGO!!! Você venceu {win} vezes.')