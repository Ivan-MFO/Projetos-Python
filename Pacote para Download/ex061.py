#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA mostrando os 10 primeiros termos da progressão usando a estrutura while

print('Gerador de PA')
print('*******************************')

termo = int(input('Digite o termo da PA: '))
razão = int(input('Digite a razão da PA: '))
primeiro = termo
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')
