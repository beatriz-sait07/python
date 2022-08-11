menor = 0
maior = 0
for pessoas in range(1,6):
    peso = float(input('peso da {}º pessoa: '. format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso eh de {}'.format(maior))
print('o menor peso eh de {}'.format(menor))

