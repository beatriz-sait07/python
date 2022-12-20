import math
num= float(input('angulo: '))
seno = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tg = math.tan(math.radians(num))
print('angulo: {}\nseno: {:.2f}\ncosseno: {:.2f}\ntangente: {:.2f}'.format(num, seno, cos, tg))
