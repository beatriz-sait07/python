lista = []

for c in range(0, 5):
    num = int(input('digite um numero: '))
    #inicio      fim
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('add no final')
    else:
        aux = 0
        #percorre a lista
        while aux < len(lista):
            #verifica se o valor digitado é menor que algma posicao da lista
            if num < lista[aux]:
                lista.insert(aux, num)
                print(f'add na posicao {aux} da lista')
                break
            aux += 1
print(lista)