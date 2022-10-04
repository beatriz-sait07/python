total = total1 = menor = cont = 0
barato = ''
while True:
    prod = input('Produto: ')
    preco = float(input('Preco, R$ '))
    cont+=1
    total += preco
    if preco > 1000:
        total1 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
    resp = ' '
    while resp not in 'sn':
        print('-' * 30)
        resp = input('Deseja continuar? [S/N]  ').lower()[0]
        print('-'*30)
    if resp == 'n':
        break
print('\n\n')
print(f'o produto mais barato eh {barato} com valor de R$ {menor}')
print(f'{total1} produtos com valor acima de R$ 1.000,00 ')
print(f'total.........R$ {total:.2f}')


