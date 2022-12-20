# tipo um de declaracao: 
print('exemplo 1: ')
teste = list()
teste.append('bia')
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = 'luana'
teste[1] = 36
galera.append(teste[:])
print(galera)

#tipo dois de declaracao:
print('\n\nexemplo 2:')
pessoa = [['jonas', 22], ['maria', 92], ['luis', 25]]
print(pessoa)
print(pessoa[1][0])
print(pessoa[2][1])
print(pessoa[0])
for para_cada_pessoa in pessoa:
    print(f'nome: {para_cada_pessoa[0]}\tidade: {para_cada_pessoa[1]}')

print('\n\nexemplo 3:')
#declarar usando um laco para o usuario entrar com os dados
cliente = []
cadastro = []
maior = menor = 0
for contador in range(0, 3):
    cliente.append(str(input('nome: ')))
    cliente.append(int(input('idade: ')))
    cadastro.append(cliente[:])
    cliente.clear() #limpa a lista para receber novos dados

print(cadastro)

for p in cadastro:
    if p[1] >= 18: #verifica se a pessoa eh maior de idade
        maior += 1
    else:
        menor += 1

print(f'ha {maior} pessoas maiores de idade e {menor} pessoas menores de idade')


