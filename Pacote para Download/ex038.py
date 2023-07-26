#escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor é maior, o segundo valor é maior ou não existe valor maior, os dois são iguais

num1 = int(input('Didite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print ('Comparando os números:')
if num1 > num2:
    print ('O primeiro valor é maior!')
elif num1 < num2:
    print ('O segundo valor é maior!')
else:
    print ('Não existe valor maior, os dois são iguais!')
