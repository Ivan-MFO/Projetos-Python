#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero a vinte, seu programa deve ler um número pelo teclado (entre 0 e 20) e mostrar por extenso

cont = ('zero','um', 'dois', 'três', 'quatro',
        'cinco', 'sies', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezeseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente ', end='')
print(f'Você digitou o número {cont[num]}')