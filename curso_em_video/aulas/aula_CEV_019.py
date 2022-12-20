''' modelos a serem criados
tuplas = ()
listas = []
dicionarios = {}
'''
print('anotacoes da explicacao')
dados = {'nome': 'pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])

dados['sexo'] = 'M' #cria um novo elemento
print(dados['sexo'])

del dados['idade'] #deleta dados 
print(dados)

filme = {'titulo': 'star wars',
        'ano': 1997,
        'diretor': 'george lucas'
}

for chaves, valores, in filme.items():
    print(f'{chaves}: {valores} ')

#parte pratica da aula
print('\n\nparte pratica da aula')
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
pessoas['nome'] = 'leandro'
print(pessoas)


#dicionario dentro da lista
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print('\n\n', brasil[0]['uf'])'''

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('unidade federativa: '))
    estado['sigla'] = str(input('sigla do estado: '))
    brasil.append(estado.copy()) #metodo de fatiamento do dicionario

# tipos formatados de print
for e in brasil: #for para os itens da lista
    for v in e.values(): #for para os itens do dicionario
        print(v, end=' ')

    
for e in brasil: #for para os itens da lista
    for k, v in e.items(): #for para os itens do dicionario
        print(f'o campo {k} tem valor {v}')
    print()

    

