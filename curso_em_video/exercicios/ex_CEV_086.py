# criando matriz 3x3 tabulada
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'valor para [{linha}][{coluna}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^6}]', end='')
    print()