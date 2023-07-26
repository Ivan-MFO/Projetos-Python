#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: Qual é o total gasto na compra, Quantos produtos custam mais de R$ 1000,00, Qual é o nome do produto mais barato
total = 0
barato = 0
caro = 0
cont = 0
menor = 0

while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        caro += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você gostaria de continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor total da compra foi de R${total:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')