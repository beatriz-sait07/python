'''
metade: descobre a metade de um valor
dobro: descobre o dobro de um valor
aumento: calcula um aumento de % em um valor
'''

# aula 107/108/109
def metade(num=0, format=False):
    resto = num/2
    return resto if not format else moeda(resto)

def dobro(num=0, format=False):
    resto = num*2
    return resto if not format else moeda(resto)

def aumento(num=0, taxa=0, format=False):
    resto = num + (num * (taxa/100))
    return resto if format is False else moeda(resto)

def diminuir(num=0, taxa=0, format=False):
    resto = num - (num * (taxa/100))
    return resto if format is False else moeda(resto)

def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:.2f}'.replace('.', ',') #transforma o primeiro parametro pelo segundo,ou seja, todos os pontos sera substituidos por virgulas

