"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie
duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas"""
numero = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        numero.append(num)
        pares.append(num)
    elif num % 2 == 1:
        numero.append(num)
        impares.append(num)
    opcao = input('Deseja continua? [S/N] ').strip().upper()[0]
    if opcao != 'S':
        break
print(f'\nLista informada: {numero}')
print(f'Pares da lista informada: {pares}')
print(f'Impares da lista informada: {impares}')
