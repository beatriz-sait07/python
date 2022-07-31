import random
al = input('1ºaluno: ')
al1 = input('2ºaluno: ')
al2 = input('3ºaluno: ')
al3 = input('4ºaluno: ')
lista = [al, al1, al2, al3]
ap = random.shuffle(lista)
print('a ordem de apresentaçao sera\n')
print(lista)