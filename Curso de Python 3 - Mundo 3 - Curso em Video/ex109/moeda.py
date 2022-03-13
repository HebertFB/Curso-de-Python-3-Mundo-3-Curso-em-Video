def aumentar(preco=0, taxa=0, formato=False):
    valor = preco + (preco * taxa/100)
    return valor if formato is False else moeda(valor)


def diminuir(preco=0, taxa=0, formato=False):
    valor = preco - (preco * taxa / 100)
    return valor if formato is False else moeda(valor)


def dobro(preco=0, formato=False):
    valor = preco * 2
    return valor if formato is False else moeda(valor)


def metade(preco=0, formato=False):
    valor = preco / 2
    return valor if formato is False else moeda(valor)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
