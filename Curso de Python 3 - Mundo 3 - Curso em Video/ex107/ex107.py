"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções."""
import moeda

num = float(input('Digite o preço: R$'))
print(f'O metade de R${num:.2f} é R${moeda.metade(num):.2f}')
print(f'O dobro de R${num:.2f} é R${moeda.dobro(num):.2f}')
print(f'Aumento de 10% temos R${moeda.aumentar(num, 10):.2f}')
print(f'Diminuir de 10% temos R${moeda.diminuir(num, 10):.2f}')
