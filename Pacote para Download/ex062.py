#Melhore o desafio 061 perguntando paea o usuário se ele quer mostrar mais alguns termos. O programa encerra quando disser que quer mostrar zero(0) termos

print('Gerador de PA')
print('*******************************')

termo = int(input('Digite o termo da PA: '))
razão = int(input('Digite a razão da PA: '))
primeiro = termo
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos você quer mostrar? '))
print('PA finalizada com {} termos mostrados'.format(total))
