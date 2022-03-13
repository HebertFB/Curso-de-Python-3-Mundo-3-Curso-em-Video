"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""
pessoa = {}
povo = []
somaIdade = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = input('Nome: ').title().strip()
    while True:
        pessoa['Sexo'] = input('Sexo: [M/F]').strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Informe o sexo corretamente!! M ou F')
    pessoa['Idade'] = int(input('Idade: '))
    povo.append(pessoa.copy())
    somaIdade += pessoa['Idade']
    while True:
        opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if opcao in 'SN':
            break
        print('Opção invalida!! Informe Sim ou Não [S/N]')
    if opcao == 'N':
        break

print(f'\nA) Total de {len(povo)} pessoas cadastradas.')
print(f'B) A média de idade é de {somaIdade/len(povo):.2f} anos.')
print('C) As mulheres cadastradas foram', end=' ')
for p in povo:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]}', end=' ')
print('\nD) As pessoas com idade acima da média são', end=' ')
for p in povo:
    if p['Idade'] > (somaIdade/len(povo)):
        print(f'{p["Nome"]}', end=' ')
