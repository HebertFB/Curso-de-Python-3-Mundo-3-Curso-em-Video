"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""
numero = []

for n in range(0, 5):
    numero.append(int(input(f'Digite o {n+1}° Número: ')))
print(f'\nForam digitados {len(numero)} números!!')
numero.sort(reverse=True)
print(f'A lista de valores, ordenada de forma decrescente é: {numero}  ')
if 5 in numero:
    print('O valor 5 foi digitado e está na lista!!')
else:
    print('O valor 5 não foi digitado!!')
