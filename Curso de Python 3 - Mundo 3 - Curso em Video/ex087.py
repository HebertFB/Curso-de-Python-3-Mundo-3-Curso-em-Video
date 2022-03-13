""" Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
valor = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior2Linha = soma3Coluna = pares = 0

for l in range(0, 3):
    for c in range(0, 3):
        valor[l][c] = int(input(f'Digite o valor para {[l, c]}: '))
print(f'------- MATRIZ -------')
for l in range(0, 3):
    for c in range(0, 3):
        if valor[l][c] % 2 == 0:
            pares += valor[l][c]
        print(f'[{valor[l][c]:^5}]', end='')
    print()
    if l == 1:
        maior2Linha = valor[l][0]
        for c in range(1, 3):
            if maior2Linha < valor[1][c]:
                maior2Linha = valor[1][c]
    if c == 2:
        soma3Coluna += valor[l][c]
print('-='*11)
print(f'Soma dos pares: {pares}')
print(f'Maior da 2° coluna: {maior2Linha}')
print(f'Soma da 3° coluna: {soma3Coluna}')
