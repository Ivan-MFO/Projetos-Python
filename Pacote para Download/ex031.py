# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço de uma passagem, colocando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas
distancia = float(input('Digite a distancia que pretende percorrer na sua viagem: '))
print('Sua escolha de destino possui uma distancia de {}Km'.format(distancia))

curta = distancia * 0.50
longa = distancia * 0.45

if distancia <= 200:
    print('O valor da sua passagem será: R${:.2f}'.format(curta))
else:
    print('O valor da sua passagem será: R${:.2f}'.format(longa))
print('Tenha uma ótima viagem!')

# De forma simplificada: preço = distancia * 0.50 if distancia <=200 else distancia * 0.45