#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles.

cont = 0
soma = 0
num = 0

num = int(input('Digite um número [999 para parar]: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou 999 então é fim de programa, foram digitados {} números que somados resultam em {}'.format(cont, soma)) #ou cont - 1, soma - 999
