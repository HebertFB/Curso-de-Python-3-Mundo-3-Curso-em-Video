"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla"""
from random import randint

numero = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), )
print(f'Os números aleatórios são: {numero}')
print(f'\nO menor número é: {min(numero)}!! E o maior número é: {max(numero)}!!')
