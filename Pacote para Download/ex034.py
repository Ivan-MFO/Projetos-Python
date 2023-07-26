#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250 calcule um aumento de 10%. Para os inferiores ou iguais, o aumeto é de 15%

pay = float(input('Digite o valor do salário R$: '))
superior = pay + (pay*10/100)
inferior = pay + (pay*15/100)

if pay <= 1250:
    print('Quem ganhava R${:.2f} agora passa a ganhar R$: {:.2f}'.format(pay, inferior))
else:
    print('Quem ganhava R${:.2f} agora passa a ganhar R$: {:.2f}'.format(pay, superior))
