from random import randint
gerador = (randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))
print('tuplas: ', end=' ')
for n in gerador:
    print(f'{n}', end=' ')
print('\nfim da tupla aleatoria')
'''funcao par o menor valor'''
print(f'o menor valor eh {min(gerador)}')
'''funcao para o maior numero'''
print(f'o maior valor eh {max(gerador)}')
