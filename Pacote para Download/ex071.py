#Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual será o valor sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Obs: considerar que o caixa possui cédulas de R$ 50, 20, 10 e 1

print('***** CAIXA ELETRÔNICO BANCO IVAN *****')
valor = int(input('Qual valor deseja sacar?: R$ '))
total = valor
montante = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        montante += 1
    else:
        if montante > 0:
            print(f'Total de {montante} cédulas de R${ced}')
        if ced == 50:
            ced =20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        montante = 0
        if total == 0:
            break
print('***** VOLTE SEMPRE *****')