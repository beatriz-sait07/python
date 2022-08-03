#transformaçao de bases
import math
n = int(input('digite um numero: '))
base = int(input('escolha um tipo de base: \nBinario -> (1), octal -> (2) ou hexadecimal -> (3)\n'))
if base == 1:
    print('a conversao escolhida foi para \033[1;36mBINARIO\033[m\nbase 10 = {}\nbase 2 = {}'.format(n, bin(n))[2:])
elif base == 2:
    print('a conversao escolhida foi para \033[1;36mOCTADECIMAL\033[m base 10 = {}\nbase 8 = {}'.format(n, oct(n)[2:]))
elif base == 3:
    print('a conversao escolhida foi para \033[1;36mHEXADECIAL\033[m\nbase 10 = {}\nbase 16 = {}'.format(n, hex(n)[2:]))
else:
    print('numero invalido!')
