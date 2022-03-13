""" Faça um programa que tenha uma função chamada área(), que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a área do terreno."""
def area(larg, comp):
    terreno = larg * comp
    print(f'\nUm terreno com {larg}ms X {comp}ms tem uma aréa de {terreno}m²!')


# Programa principal
print('Parametros do terreno')
print('=' * 22)
largura = float(input('Largura do terreno: '))
Comprimento = float(input('Comprimento do terreno: '))
area(largura, Comprimento)
