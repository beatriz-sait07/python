#tentando verificar um palindromo
letras = []
for c in range(0, 4):
    letras.append(input('digite uma letras: '))
palindromo_teste = letras[:]
palindromo_teste.reverse()
print(f'digitado: {letras}\n inverso: {palindromo_teste}\n\n')

if letras == palindromo_teste:
    print('as letras digitadas formam um palindromo')
else:
    print('as letras digitadas nao formam um palindromo')
