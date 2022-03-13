def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ocorreu um ERRO na criação do arquivo!!')
    else:
        print(f'Arquivo {nome} criado com sucesso!!')


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Ocorreu um ERRO ao ler arquivo!!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Ocorreu um ERRO na abertura do arquivo!!')
    else:
        try:
            a.write(f'{nome.title()};{idade}\n')
        except:
            print('Ocorreu um ERRO ao tentar escrever os dados!!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


def buscar(arq, nome='desconhecido'):
    try:
        buscarNome = nome.title()
        a = open(arq, 'rt')
    except:
        print('Ocorreu um ERRO ao ler arquivo!!')
    else:
        cabecalho(f'BUSCANDO {buscarNome}...')
        existe = False
        for linha in a:
            if buscarNome in linha.split(';')[0]:
                dado = linha.split(';')
                dado[1] = dado[1].replace('\n', '')
                print(f'{buscarNome} encontrado com sucesso!!')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')
                existe = True
        if not existe:
            print(f'Não existe {buscarNome} nos registros.')
    finally:
        a.close()

def deletar(arq, nome='desconhecido'):
    try:
        deletarNome = nome.title()
        a = open(arq, 'rt')
        aux = []
        aux2 = []
    except:
        print('Ocorreu um ERRO ao ler arquivo!!')
    else:
        # Copiando registro para lista auxiliar 'aux'
        for i in a:
            aux.append(i)
        # Percorre a copia auxiliar 'aux'
        for i in range(0, len(aux)):
            # Copia todos os registros de 'aux' para lista auxiliar 'aux2', menos o que será deletado
            if deletarNome not in aux[i]:
                aux2.append(aux[i])
        a = open(arq, 'wt')
        # Reescrever todos os registros atualizados de 'aux2' no arquivo original
        for i in aux2:
            a.write(i)
        print(f'O registro de {deletarNome} foi deletado com sucesso!!')
    finally:
        a.close()
