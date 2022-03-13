"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente"""
numeros = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite o {i+1} nùmero: '))
    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 == 1:
        numeros[1].append(num)

print(f'numeros: {numeros}')
numeros[0].sort()
print(f'Pares: {numeros[0]}')
numeros[1].sort()
print(f'Impares: {numeros[1]}')
