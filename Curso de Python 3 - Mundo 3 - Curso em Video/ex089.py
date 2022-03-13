"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente."""
turma = []
aluno = []
nota = [0.0, 0.0, 0.0]

while True:
    aluno.append(str(input('Nome: ')).strip().title())
    for n in range(2):
        nota[n] = float(input(f'Nota {n+1}: '))
    nota[2] = (nota[0] + nota[1]) / 2
    aluno.append(nota[:])
    nota.clear()
    nota = [0.0, 0.0, 0.0]
    turma.append(aluno[:])
    aluno.clear()
    opcao = input('Deseja continua? [S/N]').strip().upper()[0]
    if opcao != 'S':
        break
print('\n-------- BOLETIM ESCOLAR --------')
print('N#  NOME       MÉDIA')
print('-'*33)
t = 0
while t != len(turma):
    print(f'{t}   ', end='')
    for a in turma[t]:
        print(f'{turma[t][0]}       ', end='')
        for n in range(0, 2):
            print(f'{turma[t][1][2]:>10}', end='')
            break
        break
    t += 1
    print()
print('-'*33)
while True:
    aluno = int(input('Mostrar notas de que aluno (Informe o N# do aluno)? (999 interrompe): '))
    if aluno == 999:
        break
    if turma[aluno]:
        print(f'As notas de {turma[aluno][0]} são: ', end='')
        for a in turma[aluno]:
            for n in range(0, 2):
                print(f'[{turma[aluno][1][n]} - {turma[aluno][1][n+1]}]', end='')
                break
            break
        print()
        print('-' * 33)
print('Fim do Programa')
