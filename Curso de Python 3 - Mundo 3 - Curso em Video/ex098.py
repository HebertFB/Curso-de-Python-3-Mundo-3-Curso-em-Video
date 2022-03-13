"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo. Seu programa tem que realizar três contagens através da função criada:"""
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        x = i
        while x <= f:
            print(f'{x} ', end='')
            x += p
        print('FIM!')
    elif i > f:
        x = i
        while x >= f:
            print(f'{x} ', end='')
            x -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 30)
print('Informe os paramentros da contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)
