'''
metade: descobre a metade de um valor
dobro: descobre o dobro de um valor
aumento: calcula um aumento de % em um valor
'''
from time import sleep
# aula 107/108/109
def metade(preco=0, format=False):
    resto = preco/2
    return resto if not format else moeda(resto)

def dobro(preco=0, format=False):
    resto = preco*2
    return resto if not format else moeda(resto)

def aumento(preco=0, taxa=0, format=False):
    resto = preco + (preco * (taxa/100))
    return resto if format is False else moeda(resto)

def diminuir(preco=0, taxa=0, format=False):
    resto = preco - (preco * (taxa/100))
    return resto if format is False else moeda(resto)

def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:.2f}'.replace('.', ',') #transforma o primeiro parametro pelo segundo,ou seja, todos os pontos sera substituidos por virgulas

def juncao(preco=0, juros=0, desc=0):
    print('-'*43)
    print('resumo dos precos'.center(43))
    print('-'*43)
    print(f'valor original: {moeda(preco)}')
    print(f'metade do valor: {metade(preco, True)}')
    print(f'dobro do valor: {dobro(preco,True)}')
    print(f'valor com desconto de {desc}%: {diminuir(preco,desc,True)}')
    print(f'valor com acrescimo de {juros}%: {aumento(preco,juros,True)}')

def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: entre com um valor inteiro valido!\033[m')
        else:
            return inteiro

def linha(tam=42):
    return '-'*tam


def carregamento():
    print('opcao finalizar sistema: ',end=' ')
    sleep(0.2)
    print('\033[0;30;45mC\033[m', end='', flush=True)
    sleep(0.2)
    print('\033[0;30;45mA\033[m', end='', flush=True)
    sleep(0.2)
    print('\033[0;30;45mR\033[m', end='', flush=True)
    sleep(0.2)
    print('\033[0;30;45mR\033[m', end='', flush=True)
    sleep(0.2)
    print('\033[0;30;45mE\033[m', end='', flush=True)
    sleep(0.2)
    print('\033[0;30;45mG\033[m', end='', flush=True)
    sleep(0.2)
    print('\033[0;30;45mA\033[m', end='', flush=True)
    sleep(0.2)
    print('\033[0;30;45mN\033[m', end='', flush=True)
    sleep(0.2)
    print('\033[0;30;45mD\033[m', end='', flush=True)
    sleep(0.2)
    print('\033[0;30;45mO\033[m')
    sleep(0.3)
    print('\n\n\033[0;30;45mATE LOGO...\033[m')



def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def ver_cad(pessoa):
    print(linha())
    print('OPCAO 1'.center(40))
    print(linha())
    
def novo_cad(pessoa):
    print(linha())
    print('OPCAO 2'.center(40))
    print(linha())
    
def sair():
    print(linha())
    carregamento()
    
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua opcao: ')
    print()
    return opc