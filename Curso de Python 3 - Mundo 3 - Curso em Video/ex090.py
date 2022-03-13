"""Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionário. No final, mostre o conteúdo da estrutura na tela"""
aluno = {}

aluno['Nome'] = input('Nome do aluno: ')
aluno['media'] = float(input('Media do aluno: '))
if aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'
print('-'*20)
for k, v in aluno.items():
    print(f'{k} = {v}')
