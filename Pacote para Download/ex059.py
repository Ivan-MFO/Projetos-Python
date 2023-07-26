#Crie um programa que leia dois valores e mostre um menu na tela: [1] somar, [2] multiplicar, [3] maiot, [4] novos números, [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso
from time import sleep

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opção = 0

while opção != 5:

    print('''Escolha uma das opções a seguir para continuar:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do programa''')
    opção = int(input('Qual a sua opção? '))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é {}'.format(num1, num2, soma))
    elif opção == 2:
        mult = num1 * num2
        print('A multiplicação entre {} e {} é {}'.format(num1, num2, mult))
    elif opção == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior valor entre {} e {} é {}'.format(num1, num2, maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando... ')
    else:
        print('Opção inválida, tente novamente')
    print('*/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\*')
    sleep(2)
print('Fim do Programa')
