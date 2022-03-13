""" Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()).No final, mostre a lista ordenada na tela"""

numero = []

for n in range(0, 5):
    num = int(input(f'Digite o {n+1}º número: '))
    if n == 0 or num > numero[-1]:
        numero.append(num)
    else:
        posicao = 0
        while posicao < len(numero):
            if num < numero[posicao]:
                numero.insert(posicao, num)
                break
            posicao += 1
print(f'\nLista Ordenada: {numero}')

"""
lista = list()
for c in range(5):
    n = int(input("Digite o numero: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        for pos, x in enumerate(lista):
            if n <= x:
                lista.insert(pos, n)
                break
print(lista)
"""
