'''tuplas sao imutaveis'''
tupla = ('1', '3', '6','9','11','10','8','63')
print(f'tupla origem: {tupla}\n')


'''lista são mutaveis'''
lista = ['1', '3', '6','9','11','10','8','63']
print(f'lista origem: {lista}')
lista[1] = 2
print(f'lista mudando valor: {lista}')
#add valor usando append -> add apenas um valor por vez
lista.append(12)
print(f'lista add valores: {lista}')
#removendo valor do fim
lista.pop()
print(f'removendo ultimo elemento: {lista}')

'''iniciado lista vazia'''
print('\n\n')
val = []
val.append(1)
val.append(2)
val.append(3)

#imprimir bonito
print('inciando com a tupla vazia e dando valores a ela:')
for v in val:
    print(f'[{v}]', end='')

print('\n\n')
for c, v in enumerate(val):
    print(f'posicao {c} está o valor {v}')
print('\n\n')

#peculiaridade do python
a = [2,3,4,7]
b = a
print(f'lista A = {a}\nlista B = {b}')
#fazer mudanca em uma lista do modelo ligacao, alterará as duas lista
b[2] = 8
print(f'LISTA MODIFICADA\nlista A = {a}\nlista B = {b}')
#para fazer uma copia da lista e alterar a segunda voce precisa fazer o fatiamento
c = [1,2,3,5]
d = c[:]
d[1] = 3
print(f'LISTA COPIA\nlista C = {c}\nlista D = {d}')
print('\n\nFIM DA AULA')