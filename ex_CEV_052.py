num = int(input('digite um numero: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print('o {} eh um numero primo!'.format(num))
else:
    print('o {} NAO eh um numero primo!'.format(num))
