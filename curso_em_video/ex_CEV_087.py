# criando matriz, saber a: dos vetores pares, soma da terceira coluna, maior valor da segunda linha
matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_num_par = maior = soma_coluna = 0

for linha in range(0, 3): # inserindo dados na matriz
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}][{coluna}]: '))


print('-='*60)
for linha in range(0, 3): #imprimindo a matriz
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^6}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_num_par += matriz[linha][coluna]
    print()

for linha in range(0 ,3): #somando valores da 3 coluna
    soma_coluna += matriz[linha][2]

for coluna in range(0, 3): #buscando maior elemento na linha 1
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

print('-='*60)
print(f'soma de valores pares: {soma_num_par}')
print(f'soma dos elementos da terceira coluna: {soma_coluna}')
print(f'maior elemento da primeira linha: {maior}')