n = int(input('inicio da PA: '))
n1 = int(input('razao: '))
decimo = n + (10 - 1) * n1
for c in range(n, decimo + n1, n1):
    print('{}'.format(c), end='->')
print('fim')
