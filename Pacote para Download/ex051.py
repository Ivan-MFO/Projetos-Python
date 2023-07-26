#Desenvolva um programa que leia o primeiro número e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = termo + (10 - 1) * razão
for c in range(termo, décimo + razão, razão):
    print('{}'.format(c))
print('FIM')