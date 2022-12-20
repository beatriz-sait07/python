'''tempo = int(input('quantos anos tem seu carro? '))
print('versao completa!')
if tempo <= 3:
    print('carro novo!')
else:
    print('carro velho!')
print('versao simplificada! ')
print('carro novo!'if tempo<=3 else'carro velho!')
'''

'''nome = input('qual seu nome? ')
if nome.capitalize() == 'Gustavo':
    print('que nome lindo voce tem!\nBom dia {}'.format(nome))
else:
    print('prazer em conhece-lo {}'.format(nome))
'''

n1 = float(input('1º nota: '))
n2 = float(input('2ºnota: '))
media = (n1+n2)/2
if media >= 6:
    print('voce teve uma boa media!\nParabens!')
else:
    print('voce teve uma media ruim!\nEstude mais da proxima vez!')