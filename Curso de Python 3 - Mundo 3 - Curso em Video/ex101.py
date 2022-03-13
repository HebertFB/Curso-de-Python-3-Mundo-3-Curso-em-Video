""" Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
 de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO,
 OPCIONAL e OBRIGATÓRIO nas eleições."""
def vota(anoNasc):
    """
    Função que retorna a idade atual do usuario
    Param: anoAtual - Pega o ano atual do sistema
    Param: anoNasc - Pega o ano de nascimento informado pelo usario
    Param: idade - Calcula a idade atual do usuario
    Param: return - Retorna a idade atual
    """
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    if 15 < idade < 18 or idade > 60:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif 17 < idade <= 60:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: NÂO VOTO.'


# Programa Principal
ano = int(input('Em que ano você nasceu? '))
print(vota(ano))
