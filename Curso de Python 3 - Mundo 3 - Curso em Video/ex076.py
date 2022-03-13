"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular"""
print('-'*48)
print(f'{"PRODUTOS & PREÇOS":^48}')
print('-'*48)
tabela = ('Pão', 4.25, 'Manteiga', 5.99, 'Café', 8.0, 'Miojo', 2.25, 'Manzeina', 5.50, 'Bolacha', 4.50)

for posicao in range(0, len(tabela)):
    if posicao % 2 == 0:
        print(f'{tabela[posicao]:.<40}', end='')
    else:
        print(f'R${tabela[posicao]:>6.2f}')
print('-'*48)