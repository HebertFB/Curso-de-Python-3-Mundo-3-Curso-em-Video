"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista"""
numero = []
menor = 0
maior = 0
for n in range(0, 5):
    numero.append(int(input('Digite um número: ')))
    if n == 0:
        menor = maior = numero[n]
    else:
        if numero[n] > maior:
            maior = numero[n]
        if numero[n] < menor:
            menor = numero[n]
print(f'\nO maior número é {maior} e está na posição', end=' ')
for cont, valor in enumerate(numero):
    if valor == maior:
        print(f'{cont} ', end='')
print(f'\nO menor número é {menor} e está na posição', end=' ')
for cont, valor in enumerate(numero):
    if valor == menor:
        print(f'{cont} ', end='')
