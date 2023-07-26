# Faça um programa  que leia um ano qualuqer e mostre se ele é bissexto
from datetime import date

ano = int(input('Digite o ano desejado, coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano desejado é bissexto')
else:
    print('O ano desejado é normal, possui 365 dias')
