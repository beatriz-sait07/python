'''conjunto'''
print('modelo 1 de conjunto')
conj = {1, 2, 3, 4, 4, 2}
conj.add(5) #adiciona um elemento ao conjunto
conj.discard(4) #elimina um elemento
print(conj)

print('\n\n')
print('modelo 2 de conjunto: uniao')
conj1 = {0, 1, 3, 5, 7}
conj2 = {0, 2, 4, 6, 8}
conj_uniao = conj1.union(conj2)
print(f'conj1 = {conj}\nconj2 = {conj2}\nuniao conj1 & conj2 = {conj_uniao}')


print('\n\nmodelo 3 de conjunto: interseccao')
conj_inters = conj1.intersection(conj2)
print(f'conj1 = {conj}\nconj2 = {conj2}\ninterseccao conj1 & conj2 = {conj_inters}')

print('\n\nmodelo 4 de conjunto: direfenca')
conj_dif_1 = conj1.difference(conj2)
conj_dif_2 = conj2.difference(conj1)
print(f'conj1 = {conj1}\nconj2 = {conj2}\ndiferenca conj1 & conj2 = {conj_dif_1}\ndiferenca conj2 & conj1 = {conj_dif_2}')

print('\n\nmodelo 5 de conjunto: diferenca simetrica') #pega apenas os valores distintos entre os conjuntos desejados
conj_dif_simetrica = conj1.symmetric_difference(conj2)
print(f'conj1 = {conj1}\nconj2 = {conj2}\ndiferenca simetrica do conj1 & conj2 = {conj_dif_simetrica}')

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print('\n\nmodelo 6 de conjunto: subset') #saber se todos os elementos de um conjunto pertence a outro conjunto
conj_subset1 = a.issubset(b)
conj_subset2 = b.issubset(a)
print(f'conj A eh um subconjunto de B: {conj_subset1}\nconj B eh um subconjunto de A: {conj_subset2}')

print('\n\nmodelo 7 de conjunto: superset') #oposto do modelo 6
superset = a.issuperset(b)
print(superset)

print('\n\nconvertendo lista em conjunto para validacoes de dados repetidos')
lista = ['dog', 'cat', 'dog', 'elephant', 'cat']
conj_animal = set(lista)
print(conj_animal)
print('convertendo o conjunto transformado em lista novamente')
list_animal = list(conj_animal)
print(list_animal)