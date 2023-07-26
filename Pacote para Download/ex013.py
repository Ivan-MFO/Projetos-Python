#Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

s = float(input('Digite o seu salário: '))
a = s+(s*15/100)
print('Seu salário com o acréscimo é de: R${}'.format(a))
