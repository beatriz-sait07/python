from random import randint
from time import sleep
num_comp = randint(0, 5)
num_p = input('qual numero o computador pensou entre 0 - 5:\n ')
print('PROCESSANDO...')
sleep(2)
if num_p == num_comp:
    print('voce ACEROU!')
else:
    print('voce ERROU!')
print('o computador pensouno numero ',num_comp)