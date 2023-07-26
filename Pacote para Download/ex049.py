#Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher. só que agora utilizando um laço for

num = int(input('Digite um núemro de 0 a 10 para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))