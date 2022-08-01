dsc = float(input('distancia em KM: '))
if dsc <= 200:
    print('R$ {} para uma viagem de '.format(dsc * 0.5), dsc)
else:
    print('R$ {} para uma viagem de '.format(dsc * 0.45), dsc)
