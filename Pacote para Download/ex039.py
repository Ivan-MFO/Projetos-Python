#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: Se ele ainda vai se alistar no serviço militar, se é a hora de se alistar, se já passou do tempo de alistamento. Seu programa também deverá mostrar o campo que faltou ou que passou do prazo

from datetime import date
atual = date.today().year

nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))