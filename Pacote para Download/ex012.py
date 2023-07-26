#Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

n = float(input('Digite o preço do produto: '))
d = n-(n*5/100)
print('O preço do seu produto com o desconto será: R${}'.format(d))
