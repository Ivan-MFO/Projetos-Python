#A confederação nacional de natação precisa de um programador que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: até 9 anos: mirim, até 14 anso: infantil, até 19 anos: junior, até 20 anos: senior, acima de 20 anos: master

from datetime import date
atual = date.today().year
nasc = int(input('Qual o seu ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <=25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')