import random
while True:
    gerador = int(random.randint(0, 10))
    print(gerador, end=',')
    if gerador[4] < 10:
        break
print('\nfim da tupla aleatoria')
print(f'o menor valor eh {sorted(gerador[0])}')
print(f'o maior valor eh {sorted(gerador[10])}')
