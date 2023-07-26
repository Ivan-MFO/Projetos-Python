#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

palpite = 0
nupc = randint(0, 10)

print('Sou o seu computador.. Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False

while not acertou:
    nuplayer = int(input('Tente adivinhar qual número de 0 a 10 foi escolhido: '))
    palpite += 1
    if nuplayer == nupc:
        acertou = True
    else:
        if nuplayer < nupc:
            print('Mais... Tente novamente')
        elif nuplayer > nupc:
            print('Menos... Tente novamente')
print('O número escolhido pelo computador foi {} e você acertou com {} palpites.'.format(nupc, palpite))
