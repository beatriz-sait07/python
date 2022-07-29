import math
num = int(input('digite um numero: '))
raiz = math.sqrt(num)
print('a raiz de {} eh igual a {:.2}'.format(num, raiz))
print('a raiz de {} eh igual a {}'.format(num, math.ceil(raiz)))
print('a raiz de {} eh igual a {}'.format(num, math.floor(raiz)))
