def aumentar(preco=0, taxa=0):
    valor = preco + (preco * taxa/100)
    return valor


def diminuir(preco=0, taxa=0):
    valor = preco - (preco * taxa / 100)
    return valor


def dobro(preco=0):
    valor = preco * 2
    return valor


def metade(preco=0):
    valor = preco / 2
    return valor


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
