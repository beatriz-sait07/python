
num = (int(input(f'Digite o 1º = ')),
        int(input(f'Digite o 2º = ')),
        int(input(f'Digite o 3º = ')),
        int(input(f'Digite o 4º = ')))

for par in num:
    if par % 2 == 0:
        print(par, end=', ')

print(num)
print(f'voce digitou o "9" {num.count(9)} vezes')
if 3 in num:
    print(f'o valor 3 apareceu na posicao {num.index(3)+1}') 
else: print('nao teve nehum numero 3 digitado')
print(f'os valores pares sao {par}')
