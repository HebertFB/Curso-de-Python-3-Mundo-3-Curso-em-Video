"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
from time import sleep

def maior(* num):
    cont = maior = 0
    print('=' * 35)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.2)
        if cont == 0:
            maior = valor
        else:
            if valor > valor:
                maior = valor
        cont += 1
    print(f'\nForam informado {cont} valores!')
    print(f'O maior valor informado foi {maior}!\n')


# Programa Principal
maior(4, 2, 0, 1, 7)
maior(44, 12, 7)
maior()
