#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor válido.

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informação inválida, tente novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))