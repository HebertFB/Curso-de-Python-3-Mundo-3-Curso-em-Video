"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato"""
jogador = {'Nome': input('Nome do jogador: ').strip().title()}
partidas = []
jogos = int(input(f'Partidas {jogador["Nome"]} jogadas: '))
print('-'*40)
for i in range(0, jogos):
    partidas.append(int(input(f' - Gol(s) marcado(s) na {i+1}ª partida: ')))
jogador['Partidas'] = partidas[:]
jogador['total'] = sum(partidas)

print(f'---------- ESTATICAS DE {jogador["Nome"]} ----------')
for j in jogador['Partidas']:
    for i, g in enumerate(partidas):
        print(f'    {i+1}ª Partida: {g} gol(s)!!')
    break
print(f'{jogador["Nome"]} fez um total de {jogador["total"]} gol(s) em {len(jogador["Partidas"])}'
      f' partidas durante o campeonato!!')
