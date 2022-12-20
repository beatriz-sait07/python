i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('invetvalo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim!')
s = 0
for d in range(0, 3):
    n = int(input('digite um valor: '))
    s += n
print('o somatorio de todos os valores foi {}'.format(s))
print('FIM')