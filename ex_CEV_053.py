frase = input('digite uma frase: ').strip().upper()
sep = frase.split()
junto = ''.join(sep)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('eh um palindromo')
else:
    print('nao eh um palindromo!')

'''
frase = input('digite uma frase: ').strip().upper()
sep = frase.split()
junto = ''.join(sep)
inverso = junto[::-1]
if inverso == junto:
    print('eh um palindromo')
else:
    print('nao eh um palindromo!')

'''
