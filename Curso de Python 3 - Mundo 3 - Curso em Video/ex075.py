"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares """
valores = (int(input('Informe o 1° valor: ')), int(input('Informe o 2° valor: ')),
           int(input('Informe o 3° valor: ')), int(input('Informe o 4° valor: ')))

print(f'\nO número 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O primeiro número 3 apareceu na posição {valores.index(3)+1}')
else:
    print(f'O número 3 não foi digitado')
print('Os números pares digitados são: ', end='')
for num in valores:
    if num % 2 == 0:
        print(f'{num}', end=' ')
