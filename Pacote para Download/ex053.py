#Crie um programa que lei uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
over = ''
print('O inverso de {} é {}'.format(junto, over))
for letra in range(len(junto) - 1, -1, -1):
    over += junto[letra]
if over == junto:
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo')