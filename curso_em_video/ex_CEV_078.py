lista = []
maior = 0
menor = 0

for n in range(0,5):
    lista.append(int(input(f'digite um valor para a posicao {n}: ')))
    if n == 0:
        maior = lista[n]
        menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]

        if lista[n] < menor:
            menor = lista[n]
            
print(f'\n\nvoce digitou os valores {lista}')
print(f'o maior valor eh: {maior} e esta na(s) posicao(oes)', end='')
for c,i in enumerate(lista):
    if i == maior:
        print(f'[{c}]', end='')

print('\n')
print(f'o menor valor eh: {menor} e esta na(s) posicao(oes)',end='')
for c,i in enumerate(lista):
    if i == menor:
        print(f'[{c}]', end='')
print('\n')
        