""" Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar"""
from datetime import date
pessoa = {}
pessoa['Nome'] = input('Nome: ').title().strip()
nasc = int(input('Ano de nascimento: '))
pessoa['Idade'] = date.today().year - nasc
ctps = int(input('Carteira de Trabalho (0 não tem): '))

if ctps != 0:
    pessoa['Carteira'] = ctps
    ctpsAno = int(input('Ano de contratação: '))
    pessoa['Ano de Contratacao'] = date.today().year - ctpsAno
    pessoa['Salario'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = (pessoa["Idade"] - pessoa["Ano de Contratacao"]) + 35
    print('-'*30)
    for k, v in pessoa.items():
        print(f'   - {k} tem o valor: {v}')
