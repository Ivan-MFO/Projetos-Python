#Crie um programa que leia vários números inteiros pelo teclado. No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

soma = média = maior = menor = cont = 0
stop = 'S'

while stop in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    stop = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
média = soma / cont
print('Você digitou {} números e a média entre eles é de {}'.format(cont, média))
print('O menor número digitado foi {} e o maior número digitado foi {}'.format(menor, maior))
