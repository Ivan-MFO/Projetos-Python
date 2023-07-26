#Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes a letra "a" aparece, em que posição ela aparece a primeira vez, em que posição ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).lower().strip()
print ('Analizando a frase: ')
print ('A frase possui quantas letras A: {}'.format(frase.count('a')))
print ('Qual a primeira posição da letra A na frase: {}'.format(frase.find('a')+1))
print ('Qual a ultima posição da letra A na frase: {}'.format(frase.rfind('a')+1))
