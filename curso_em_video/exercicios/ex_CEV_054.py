from datetime import date
cont = 0
cont1 = 0
for verif in range(1, 8):
    nsc = int(input('ano que {} nasceu: '.format(verif)))
    atual = date.today().year
    idade = atual - nsc
    if idade >= 21:
       cont += 1
    else:
        cont1 += 1
print('ha {} maiores de idade\nha {} menores de idade'.format(cont, cont1))
