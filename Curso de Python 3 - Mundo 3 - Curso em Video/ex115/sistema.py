from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'listadecadastros.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Buscar Pessoa', 'Cadastrar nova Pessoa', 'Deletar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de buscar registro de pessoa no arquivo
        nome = input('Buscar: ')
        buscar(arq, nome)
    elif resposta == 3:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRADO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 4:
        # Opção de deletar registro de pessoa no arquivo
        nome = input('Deletar: ')
        deletar(arq, nome)
        sleep(0.5)
        lerArquivo(arq)
        sleep(2)
    elif resposta == 5:
        # Opção de sair do sistema
        cabecalho('Saindo do sistema... Até Logo!')
        break
    else:
        # Digitou uma opção invalida
        print('\033[31mERRO!! Digite uma opção valida!\033[m')
    sleep(0.7)
