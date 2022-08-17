prim = int(input('inicio da PA: '))
razao = int(input('razao: '))
termo = prim
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('quantos termos voce deseja acrescentrar: '))
print('houve um total de {} termos'.format(total))
print('fim')