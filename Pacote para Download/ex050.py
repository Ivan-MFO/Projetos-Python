#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for impar desconsidere-o

soma = 0
for c in range(1, 7):
        num = int(input('Digite o {} número: '.format(c)))
        if num % 2 ==0:
            soma += num
print('A soma dos números pares entre os 6 valores é de: {}'.format(soma))