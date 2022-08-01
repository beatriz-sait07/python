import random
num_comp = random.randint(0,5)
num_p = input('qual numero o computador pensou entre 0 - 5:\n ')
if num_p == num_comp:
    print('voce acertou!')
else:
    print('voce errou!')
print('o computador pensouno numero ',num_comp)