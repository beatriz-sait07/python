from random import randint
from time import sleep
from operator import itemgetter


jogadores = {'jogador1': randint(1,6), 
            'jogador2': randint(1,6),
            'jogador3': randint(1,6),
            'jogador4': randint(1,6)}

ranking = list()

print('valores sorteados: ')
for ind, v in jogadores.items():
    print(f'o {ind} tirou {v} no dado...')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*5, end='')
print(' RANKING ', end='')
print('-='*5)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)

