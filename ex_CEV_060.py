from math import factorial
fat = int(input('numero que deseja o fatorial: '))
n = factorial(fat)
print('{}! = {}'.format(fat, n))

'''*************usando o while************
fat = int(input('numero que deseja o fatorial: '))
n = fat
f = 1
while n > 0:
    print('{}'.format(n), end=' ')
    print('x' if n > 1 else ' = ', end=' ')
    f *= n
    n -= 1
print('{}'.format(f))'''

