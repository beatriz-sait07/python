'''tupla -> lanche = ('elemento 1','elemento 2',' elemento 3','elemento4') **imutaveis**

listas -> lanche = ['elemento 1','elemento 2',' elemento 3','elemento 4'] **mutaveis** -sando .append
'''

tupla = (2, 5 , 9, 1) #tupla
# num[2] = 3 da erro no cod porque tuplas sap imutaveis
print(f'tupla: {tupla}')

lista = [2, 5, 9, 1]
print(f'lista original: {lista}')
lista[2] = 3 #isto passa a ser verdade porque listas sao mutaveis
print(f'lista com novo elemento: {lista}')
lista.append(12)
print(f'lista usando append: {lista}')
lista.insert(2, 7)
print(f'lista usando insert: {lista}')
lista.sort()
print(f'lista em ordem crescente: {lista}')
lista.sort(reverse=True)
print(f'lista em ordem decrescente: {lista}')
lista.pop()
print(f'lista usando pop: {lista}')
lista.remove(2)
print(f'lista usando remove: {lista}')
print(f'tamanho da lista: {len(lista)}\n\ntestes:')

#testando imprimir valores e posicoes da lista com valores fixos
teste = [] # modo 1 para criar lista
teste.append(5)
teste.append(9)
teste.append(4)

#v -> para cada valor em teste
for indice, v in enumerate(teste):
    print(f'na posicao {indice} esta o valor {v}' )


#testando imprimir valores e posicoes da lista com valores inseridos pelo usuatio
teste1 = list() # modo 2 para criar lista
for cont in range(0 ,5): #definindo o tamanho da lista, ou seja inicio e fim
    teste1.append(int(input('digite um valor para inserir na lista: ')))
print(f'lista teste: {teste1}\n\n')

# PECULIARIDADES DA LINGUAGEM PYTHON COM RELACAO A LISTAS
list1 = [2, 4, 6, 8]
#list2 = list1 #faz uma ligacao de listas e nao uma copia, nisso ao trocar um elementod e qualquer lista a outra tambem havera a MESMA troca
list2 = list1[:] #faz uma copia de todos os elementos da lista 1, nisso ao trocar um elemento de qualquer lista a outra nao tera alteracoes
print(f'listas originais:\nlista 1: {list1}\nlista 2: {list2}')
list2[2] = 9 #ao mudar um elemento de lista espelho, voce tambem muda a lista principal p
print(f'listas com trocas:\nlista 1: {list1}\nlista 2: {list2}')


print('fim da aula')