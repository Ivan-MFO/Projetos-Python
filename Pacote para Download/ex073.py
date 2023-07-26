#Crie uma tupla preenchida com os vinte primeiros colocados doi campeonato brasileiro de futebol, em ordem de colocação. Mostre: os 5 primeiros times, os 4 últimos colocados, times em ordem alfabética e em que posição está o time do Chapecoense

times = ('Botafogo', 'Flamengo', 'Grêmio', 'São Paulo',
        'Fluminense', 'Palmeiras', 'Bragantino',
        'Atlético-PR', 'Fortaleza', 'Cruzeiro', 'Internacional',
        'Atlético-MG', 'Cuiabá', 'Santos', 'Corinthians',
        'Bahia', 'Goias', 'Coritiba', 'Vasco', 'Atletica-MG')
print('*' * 282)
print(f'Os 5 primeiros colocados do campeonato são:{times[0:5]}')
print('*' * 282)
print(f'Os últimos 4 colocados do campeonato são:{times[-4:]}')
print('*' * 282)
print(f'Em ordem alfabética a lista fica:{sorted(times)}')
print('*' * 282)
print(f'O time do Vasco se encontra na {times.index("Vasco")+1}@ posição da tabela do campeonado')
print('*' * 282)