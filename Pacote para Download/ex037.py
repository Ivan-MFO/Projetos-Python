#Escreva um programa que leia um número inteiro qualquer e peça pata o usuário escolher qual será a base de conversão: 1 para Binário, 2 para Octal e 3 para Hexadecimal

num = int(input('Digite um número inteiro qualquer: '))
print ('''Escolha uma das basas de conversão: 
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal''')

opçao = int(input('Digite a sua opção: '))
if opçao == 1:
    print ('{} convertido para Binário é {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print ('{} convertido para Octal é {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print ('{} convertido para Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print ('Opção inválida!')
