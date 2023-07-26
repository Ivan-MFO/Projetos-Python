#Crie um programa que leia o nome completo de uma pessoa e mostre: nome com todas as letras maíscula, o nome com todas as minúsculas, quantas letras totais (sem considerar espaços), quantas letras o primeiro nome tem

nome = str(input('Digite seu nome completo: ')).strip()
print ('Analizando seu nome: ')
print ('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print ('Seu nome em minúsculas é: {}'.format(nome.lower()))
print ('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
div = nome.split()
print ('Seu primeiro nome é {} e ele tem {} letras'.format(div[0], len(div[0])))
