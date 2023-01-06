from modularizacao import *
def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro: nao foi possivel criar arquivo!')
    else:
        print(f'arquivo {nome} criado com sucesso!')

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True

def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO: nao foi possivel ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.readlines())