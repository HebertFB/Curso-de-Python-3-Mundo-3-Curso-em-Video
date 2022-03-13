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


def resumo(p=0, aum=15, dim=10):
    print('_' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('_' * 30)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{aum}% de aumento: \t{aumentar(p, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(p, dim, True)}')
    print('_'*30)
