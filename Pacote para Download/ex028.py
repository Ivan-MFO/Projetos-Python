#Escreva um programa que faça o computador "pensar" em um número inteiro entrei 0 e 5 e peça para o usuário tentar adivinhar qual o número escolhido. O programa devera escrever na tela se o programa venceu ou perdeu

from random import randint

nupc = randint(0, 5)

print('-=-' * 20)
nuplayer = int(input('Tente adivinhar qual número de 0 a 5 foi escolhido: '))
print('-=-' * 20)

if nupc == nuplayer:
    print('Você venceu!')
else:
    print('O computador venceu!')
print('O número escolhido pelo computador foi: {}'.format(nupc))
