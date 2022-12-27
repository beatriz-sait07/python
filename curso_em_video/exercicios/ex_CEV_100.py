from random import randint

def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(0, 10))
    print(f'lista aleatoria: {lista}')
def soma_par(lista):
    cont = 0
    for c in lista:
        if c % 2 == 0:
            cont += c
    print(f'soma dos numeros pares encontrado na lista {lista}: {cont}')


num = list()
sorteia(num)
soma_par(num)