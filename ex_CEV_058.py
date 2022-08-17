from random import randint
from time import sleep
comp = randint(0, 10)
usuario = int(input('qual numero voce acha que o computador escolher ? '))
print('processando...')
sleep(0.5)
if usuario != comp:
    print('voce ERROU!!')
    while usuario != comp:
        usuario = int(input('nova tentativa: '))
        sleep(0.3)
    print('voce ACERTOU!!!')
print('\n*** fim de jogo ***')
