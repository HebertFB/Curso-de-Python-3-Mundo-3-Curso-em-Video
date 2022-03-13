"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mO usuario não informou os dados!\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mO usuario não informou os dados!\033[m')
            return 0
        else:
            return real


# Programa Principal
i = leiaInt('Digite um inteiro: ')
f = leiaFloat('Digite um float: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f:.1f}')
