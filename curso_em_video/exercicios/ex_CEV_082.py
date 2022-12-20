lista =[]
par = []
impar = []

while True:
    lista.append(int(input('Digite um numero: ')))
    quest = input('Deseja continuar[S/N] ?\nresp: ')
    if quest in 'Nn':
        break
    if quest not in 'SsNn':
        print('digito invalido!')
        quest = input('Deseja continuar[S/N] ?\nresp: ')
    
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'lista digitada pelo usuario: {lista}')
print(f'numero PARES da lista principal: {par}')
print(f'numero IMPARES da lista principal: {impar}')
