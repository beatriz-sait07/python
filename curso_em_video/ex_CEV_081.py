lista = list()

while True:
    num = int(input('digite um numero: '))
    lista.append(num)
    quest = input('deseja continuar[S/N] ?\nresp: ')
    
    if quest in 'Nn':
        break
print(f'\nlista : {lista}')
lista.sort(reverse=True)
print(f'ordem decrescente da lista: {lista}')
print(f'foram digitados {len(lista)}')
if 5 in lista:
    print(f'o numero 5 apareceu {lista.count(5)}')
else:
    print('nao ha numero 5 nesta lista!')
    