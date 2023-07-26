#Crie um programa que tenha uma tupla com várias palavras (não usar acento). Depois disso, você deve mostrar, para cada palavra, quais são as vogais.
palavras = ('programar', 'caminhar', 'caminho', 'passo',
            'tentar', 'luta', 'desafio', 'correria',
            'superaçao')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
