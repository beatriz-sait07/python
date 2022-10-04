from random import randint
from time import sleep
comp = randint(0, 10)
palpite = 0
usuario = int(input('qual numero voce acha que o computador escolher ? '))
print('processando...')
sleep(0.5)
if usuario != comp:
    print('voce ERROU!!')
    while usuario != comp:
        usuario = int(input('nova tentativa: '))
        palpite += 1
        sleep(0.3)
    print('voce ACERTOU!!!')
print('\nvoce precisou de {} chances para acertar'.format(palpite + 1))
print('\n*** fim de jogo ***')
