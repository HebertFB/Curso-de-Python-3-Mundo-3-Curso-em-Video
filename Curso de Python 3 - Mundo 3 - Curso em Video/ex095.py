"""Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""
time = []
jogador = {}
gols = []

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ').title().strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for i in range(0, partidas):
        gols.append(int(input(f'  Quantos gols na partida {i+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
        print('Opção invalida!! Informe Sim ou Não [S/N]')
    if opcao == 'N':
        break

print('-' *40)
print('Cod  ', end= '')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 p/ parar) '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! Não existe jogador de código {busca}!')
    else:
        print(f'--- LEVATAMENTO DO JOGADOR {time[busca]["nome"]} ---')
        for p, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {p+1} fez {g} gols.')
    print('-' * 40)
print('<< FIM >>')
