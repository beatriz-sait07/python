#criar jogos da mega sena
from random import randint
from time import sleep

cont = 0
aux = 1
jogo = []
conj_jogos = []
quant_jogos = int(input('quantos jogos voce deseja que seja sorteados ?  '))

print('*'*30)
print('      JOGO DA MEGA SENA')
print('*'*30)

while aux <= quant_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    conj_jogos.append(jogo[:])
    jogo.clear()
    aux += 1
for ind, list in enumerate (conj_jogos):
    print(f'jogo {ind+1}: {list}')
    sleep(1)
