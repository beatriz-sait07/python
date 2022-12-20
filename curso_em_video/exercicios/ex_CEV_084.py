cliente = []
cadastro = []
maior_peso = menor_peso = 0

while True:
    cliente.append(str(input('Nome: ')))
    cliente.append(float(input('Peso: ')))
    if len(cadastro) == 0: 
        maior_peso = menor_peso = cliente[1]
    else:
        if cliente[1] > maior_peso:
            maior_peso = cliente[1]
        if cliente[1] < menor_peso:
            menor_peso = cliente[1]
    cadastro.append(cliente[:]) # puxa os dados inseridos na lista cliente e armazena na lista cadastro
    cliente.clear() #limpa a lista cliente
    quest = input('deseja continuar [S/N] ?  ')
    if quest in 'nN':
        break

print('-=' * 50)
print(f'voce cadastrou {len(cadastro)} pessoas')
print(f' o maior peso foi de {maior_peso}Kg, sendo de : ', end ='')
for p in cadastro:
    if p[1] == maior_peso:
        print(f'{p[0]}', end=', ')
print()
print(f'o menor peso foi de {menor_peso},Kg sendo de: ', end='')
for p in cadastro:
    if p[1] == menor_peso:
        print(f'{p[0]}', end=', ')
print()