'''num = float(input('cateto oposto: '))
num1 = float(input('cateto adjacente: '))
hi = (num ** 2 + num1 ** 2) ** (1/2)
print('hipotenusa eh {:.2}'. format(hi))'''

import math
num = float(input('cateto oposto: '))
num1 = float(input('cateto adjacente: '))
hi = math.hypot(num, num1)
print('hipotenusa = {:.2}'.format(hi))