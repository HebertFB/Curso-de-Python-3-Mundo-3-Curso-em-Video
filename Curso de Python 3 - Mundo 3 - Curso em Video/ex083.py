"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.Seu aplicativo
deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta"""
expressao = str(input('Informe a expressão: '))
parent = []

for v in expressao:
    if v == "(":
        parent.append('(')
    elif v == ")":
        if len(parent) > 0:
            parent.pop()
        else:
            parent.append(')')
            break

print(f'Parentese1: {parent}')
if len(parent) == 0:
    print('Expressão está correta!!')
else:
    print('Expressão NÃO está correta!!')
