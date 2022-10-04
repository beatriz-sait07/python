import random
import time
print('escolhas:\n\033[1;35m[0] - pedra\033[m\n\033[1;35m[1] - papel\033[m\n\033[1;35m[2] - tesoura\033[m')
itens = ('pedra', 'papel', 'tesoura')
jg1 = input('o que deseja jogar: ')
jg2 = random.randint(0,2)
print('\n\033[1;33mJO\nKEN\nPO\n\033[m')
time.sleep(.5)
print('*************************************')
print('\ncomputador jogou \033[1;33m{}\033[m\n'.format(itens[jg2]))
print('*************************************')
if jg1 == '0' and jg2 == 1 or jg1 == '1' and jg2 == 2 or jg1 == '2' and jg2 == 3:
    print('\033[1;36mEMPATE\033[m')
elif jg1 == '0' and jg2 == 3 or jg1 == '1' and jg2 == 1 or jg1 == '2' and jg2 == 2:
    print('\033[1;31m\nVOCE PERDEU!')
else:
    print('\033[1;32m\nVOCE GANHOU')