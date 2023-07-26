#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

n = float(input('Qual o valor que você possui em sua carteira?: '))
r = n/3.27
print('Voce consegue comprar {:.2f} dólares'.format(r))
