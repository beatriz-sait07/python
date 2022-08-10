print('digite seis numeros abaixo: ')
s = 0
cont = 0
for c in range(1, 7):
    num = int(input('{} = '.format(c)))
    if num % 2 == 0:
        s += num
print('a soma dos numeros pares eh de {}'.format(s))