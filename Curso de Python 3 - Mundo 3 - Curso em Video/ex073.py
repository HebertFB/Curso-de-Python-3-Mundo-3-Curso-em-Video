"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense """
tabelaColocacao = ('Atlético - MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo',
                   'Corinthians', 'Atlético - GO', 'Ceará', 'Athletico - PR', 'Internacional',
                   'Santos', 'São Paulo', 'Juventude', 'Cuiabá', 'Bahia',
                   'Fluminense', 'Grêmio', 'Sport', 'América - MG', 'Chapecoense')
print('-'*100)
print(f'Tabela do Brasileirão 2021:   {tabelaColocacao}')
print('-'*100)
print(f'Os 5 primeiros colocados são: {tabelaColocacao[:5]}')
print('-'*100)
print(f'Os últimos 4 colocados são:   {tabelaColocacao[-4:]}')
print('-'*100)
print(f'A ordem alfabética: {sorted(tabelaColocacao)}')
print('-'*100)
print(f'O time da Chapecoense está na posição: {tabelaColocacao.index("Chapecoense")+1}')
