"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso"""
numEscritos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
               'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
               'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
opcao = 'S'
while opcao == 'S':
    while True:
        numero = int(input('Informe um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print(f'\nNúmero inválido!!!', end='')
    print(f'O número informado é {numEscritos[numero]}!!')
    opcao = input('\nDeseja continuar? [S/N] ').strip().upper()[0]
