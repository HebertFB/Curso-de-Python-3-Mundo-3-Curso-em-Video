"""Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta"""
valor = [[[], [], []], [[], [], []], [[], [], []]]

for l in range(0, 3):
    for v in range(0, 3):
        valor[l][v].append(int(input(f'Digite o valor para {[l, v]}: ')))
print(f'--------- MATRIZ ---------')
for l in range(0, 1):
    for v in range(0, 3):
        print(f'{valor[v]} ')
