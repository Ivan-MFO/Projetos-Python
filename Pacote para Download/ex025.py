#Crie um programa que lia o nome de uma pessoa e diga se ele possui "silva" no nome

nome = str(input('Digite o nome: ')).strip()
print ('Exite o nome Silva neste nome?: {}'.format('SILVA' in nome.upper()))
