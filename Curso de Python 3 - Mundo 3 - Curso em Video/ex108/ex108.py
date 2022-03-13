"""Adapte o código do desafio #107, criando uma função adicional chamada moeda() que
consiga mostrar os números como um valor monetário formatado."""
import moeda

num = float(input('Digite o preço: R$'))
print(f'O metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumento de 10% temos {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Diminuir de 10% temos {moeda.moeda(moeda.diminuir(num, 10))}')
