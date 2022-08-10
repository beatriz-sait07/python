n = 0
cont = 0
for mult in range(1, 501, 2):
    if mult % 3 == 0:
        n += mult
        cont += 1
print('a soma de todos os {} valores eh de {}'.format(cont, n))