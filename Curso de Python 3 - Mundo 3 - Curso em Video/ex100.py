"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior."""
from random import randint

def sorteia(lista):
    for v in range(0, 5):
        num = randint(1, 10)
        lista.append(num)
    print(f'Números sorteados: {lista}')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nA soma do números pares é {soma}!')


#Programa Principal
numeros = []
sorteia(numeros)
somaPar(numeros)
