"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""
def notas(* nota, sit=False):
    """
    -> Função para analisar notas e situações de varias alunos
    param nota: uma ou mais notas dos alunos (aceita varias)
    param sit: valor opcional, indicando se deve ou não adicionar a situação
    return: dicionario com varias informações sobre a situação da turma
    """
    media = sum(nota) / len(nota)
    dic = {}
    dic['total'] = len(nota)
    dic['maior'] = max(nota)
    dic['menor'] = min(nota)
    dic['média'] = media
    if sit:
        if media < 5:
            dic['situação'] = 'RUIM'
        elif media < 7:
            dic['situação'] = 'BOA'
        else:
            dic['situação'] = 'EXCELENTE'
    print('_' * 80)
    return dic

# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
