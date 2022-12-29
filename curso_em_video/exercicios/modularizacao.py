'''
metade: descobre a metade de um valor
dobro: descobre o dobro de um valor
aumento: calcula um aumento de % em um valor
'''


def metade(num=0):
    return num/2

def dobro(num=0):
    return num*2

def aumento(num=0, taxa=0):
    return num + (num * (taxa/100))

def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:.2f}'.replace('.', ',') #transforma o primeiro parametro pelo segundo,ou seja, todos os pontos sera substituidos por virgulas

