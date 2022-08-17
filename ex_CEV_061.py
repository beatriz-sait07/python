prim = int(input('inicio da PA: '))
razao = int(input('razao: '))
termo = prim
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('fim')
