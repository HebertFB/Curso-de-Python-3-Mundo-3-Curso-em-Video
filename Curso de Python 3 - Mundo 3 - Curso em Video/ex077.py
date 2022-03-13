"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais"""
palavras = ('Plenitude', 'Descoberta', 'Rainha', 'Selos', 'Lunar',
            'Biplano', 'Aparar', 'Aluguel', 'Explorar', 'Inglaterra')
for posicao in palavras:
    print(f'\nA palavra {posicao.upper()} tem as vogais: ', end='')
    for letras in posicao:
        if letras.upper() in 'AEIOU':
            print(letras.upper(), end=' ')
