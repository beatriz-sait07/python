lista = list()
while True:
    #valida os numeros que estao entrando
    num = int(input('digite um valor: '))
    
    #verifica se o numero NÃO está na lista, caso nao esteja ele add
    if num not in lista:
        lista.append(num)
        print(f'valor {num} adicionado')
    else:
        print('valores duplicados nao sao aceitos')
    
    #ponto de parada do sistema
    quest = input('deseja continuar[S/N] ?\nresp: ')
    
    #se o usuario nao quiser continuaar, ele para!
    if quest in 'nN':
        break
    
#orndenação da lista
lista.sort()
print(f'os numeros digitados sao {lista}')