dsc = float(input('distancia em KM: '))
print('para uma viagem de {} KM voce gastara:'.format(dsc))
if dsc <= 200:
    print('R$ {}'.format(dsc * 0.5))
else:
    print('R$ {} '.format(dsc * 0.45))
