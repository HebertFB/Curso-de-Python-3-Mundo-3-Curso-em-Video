"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta"""
from random import randint
from time import sleep
palpites = [0, 0, 0, 0, 0, 0]
jogos = []
quqntJogos = int(input('Quantos palpites de jogos voçê deseja? '))

for i in range(0, quqntJogos):
    for j in range(0, 6):
        palpites[j] = randint(0, 60)
    palpites.sort()
    jogos.append(palpites[:])
print(f'------ Sorteando {quqntJogos} palpites ------')
for i in range(0, quqntJogos):
    sleep(1)
    print(f'Jogo {i+1}: {jogos[i]}')
