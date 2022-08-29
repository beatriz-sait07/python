'''*while tre* � um loop infinito ate voce colocar um ponto de parada *break*'''
n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
#print('soma: {}'.format(s)) --> formar antiga de escrever
print(f'soma {s}') #nova forma de escrever