# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: Quatas pessoas tem mais de 18 anos, quantos homens foram cadastrados, quantas mulheres tem menos de 20 anos

maior = 0
menor = 0
totH = 0

while True:
    print('Programa de Cadastro')
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        menor += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar a cadastrar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram cadastradas: {maior} pessoas com mais de 18 anos, {totH} Homens e {menor} mulheres com menos de 20 anos.')