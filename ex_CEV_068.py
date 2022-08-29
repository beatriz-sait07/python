import random
import time
cont = soma = perd = emp = 0
print('-'*40)
print('       jogo de impar ou par')
print('-'*40)
while True:
    comp = random.randint(1, 10)
    jg1 = int(input('escolha sua opcao: '))
    soma = comp + jg1
    if soma % 2 == 0:
        if comp % 2 == 0:
            perd = 1
            time.sleep(0.5)
            print('VOCE PERDEU!!')
            print(f'o computador jogou {comp}')
        elif comp % 2 == 1:
            cont += 1
            time.sleep(0.5)
            print('VOCE GANHOU!!')
            print(f'o computador jogou {comp}')
            print('-'*30)
        else:
            time.sleep(0.5)
            print('EMPATE!!')
            print('-'*30)
    else:
        if comp % 2 == 0:
            cont += 1
            time.sleep(0.5)
            print('VOCE GANHOU!!')
            print(f'o computador jogou {comp}')
            print('-'*30)
        elif comp % 2 == 1:
            perd = 1
            time.sleep(0.5)
            print('VOCE PERDEU!!')
            print(f'o computador jogou {comp}')
        else:
            time.sleep(0.5)
            print('EMPATE!!')
            emp += 1
            print('-'*30)

    if perd == 1:
        break
time.sleep(1)
print(f'\n\nvoce ganhou {cont}X e empatou {emp}X')
print('FIM DE JOGO!!')
