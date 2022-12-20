mult = cont = 0
while True:
    print('-'*30)
    n = int(input('qual tabuada voce deseja?  Resp: '))
    print('-'*30)
    cont = 0
    if n < 0:
        break
    if cont == 0:
        while cont < 10:
            print(f'{n} x {cont} = {n*cont}')
            cont += 1
print('foi inserido um numero negativo, sistema finalizado')