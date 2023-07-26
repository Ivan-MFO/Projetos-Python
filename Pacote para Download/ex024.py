#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

nome = str(input('Digite o nome da cidade: ')).strip()
print (nome[0:5].lower() == 'santo')
