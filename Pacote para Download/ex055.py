# Faça um programa que leia o peso de cinco pesosas. No final, mostre qual foi o maior e o menor peso lidos

totmaior = 0
totmenor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p ==1:
        totmaior = peso
        totmenor = peso
    else:
        if peso > totmaior:
            totmaior = peso
        if peso < totmenor:
            totmenor = peso
print('O maior peso lido foi de {}Kg'.format(totmaior))
print('E o menor peso lido foi de {}Kg'.format(totmenor))