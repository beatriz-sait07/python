#separar impar e par
lista_princ = [], []
num = 0

for c in range(1 , 8):
    num = (int(input(f'digite um valor para {c}: ')))
    if c % 2 == 0:
        lista_princ[0].append(num)
    else:
        lista_princ[1].append(num)
print(f'\nlista na ordem em que foi digitada\nnumeros pares: {lista_princ[0]}\nnumeros impares: {lista_princ[1]}')
lista_princ[0].sort()
lista_princ[1].sort()
print(f'\nlista ordenada em ordem crescente:\nnumeros pares: {lista_princ[0]}\nnumeros impares: {lista_princ[1]}')