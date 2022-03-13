"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em
uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente"""
numero = []
opcao = 'S'

while True:
    num = int(input('Digite um número: '))
    if num not in numero:
        numero.append(num)
        print(f'Número adicionado com sucesso!!!')
    else:
        print(f'Número NÃO adicionado, pois já existi na lista!!!')
    opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if opcao != 'S':
        break
print('-'*40)
numero.sort()
print(f'Os números informados foram: {numero}')
