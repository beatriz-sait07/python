import random
import time
print('escolhas:\n 1)pedra\n2)papel\n3)tesoura')
jg1 = input('o que deseja jogar: ')
jg2 = random.randint(1, 4)
print('\033[1;31mPENSANDO\033[m')
time.sleep(2)
print('computador jogou {}'.format(jg2))
if jg1 == '1' and jg2 == 1 or jg1 == '2' and jg2 == 2 or jg1 == '3' and jg2 == 3:
    print('\033[1;36mEMPATE\033[m')
elif jg1 == '1' and jg2 == 3 or jg1 == '2' and jg2 == 1 or jg1 == '3' and jg2 == 2:
    print('\033[1;31mVOCE PERDEU!')
else:
    print('\033[1;32mVOCE GANHOU')