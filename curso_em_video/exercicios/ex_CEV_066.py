soma = cont = 0
while True:
    n = int(input('Digite um numero: [999 - parada]'))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'foram {cont} numeros\nsoma: {soma}')