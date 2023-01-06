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
        for linha in a:
            dado = linha.split(';') #retira os ;
            dado[1] = dado[1].replace('\n', '') #substitui os \n por nada
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
def cadastrar(file, name='desconhecido', age=0):
    try:
        a = open(file, 'at')
    except:
        print('ERRO: nao foi possivel abrir o arquivo!')
    else:
        try:
            a.write(f'{name};{age}\n')
        except:
            print('ERRO: transcricao de dados nao foi efetivada!')
        else:
            print(f'{name} registrado com sucesso!')
            a.close
