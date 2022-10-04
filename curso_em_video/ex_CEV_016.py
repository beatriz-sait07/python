'''*****usando a biblioteca math geral****
import math
num = float(input('digite um valor: '))
print('o valor {} tem a parte inteira de {}'. format(num, math.trunc(num)))

*****usando a biblioteca math especifica****
from math import trunc
num = float(input('digite um valor: '))
print('o valor {} tem parte inteira de {}'.format(num, trunc(num)))
'''

'''usando sem biblioteca'''
num = float(input('digite uma valor: '))
print('o valor {} tem a parte inteira de {}'.format(num, int(num)))