#Faça um programa que mostre a tabuada de vários números, em de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print(' ********** PROGRAMA DA TABUADA ********** ')
print("Quer ver a tabuada de qual número?")

while True:
    num = int(input('Digite o número desejado: '))
    if num <0:
        break
    print('-=' * 10)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-=' * 10)
print('FIM DO PROGRAMA')
