'''
metade: descobre a metade de um valor
dobro: descobre o dobro de um valor
aumento: calcula um aumento de % em um valor
'''

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
