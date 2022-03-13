"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
pessoas = []
dados = []
leve = pesado = 0

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        leve = pesado = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opcao = input('Deseja continua? [S/N]').strip().upper()[0]
    if opcao != 'S':
        break
print('-'*40)
print(f'Foram cadastradas {len(pessoas)} pessoas!!')
print(f'Maior peso foi de {pesado}KGs. Peso repectivos de ', end='')
for i in pessoas:
    if i[1] == pesado:
        print(f'[{i[0]}] ', end='')
print(f'\nMenor peso foi de {leve}KGs. Peso repectivos de ', end='')
for i in pessoas:
    if i[1] == leve:
        print(f'[{i[0]}] ', end='')
