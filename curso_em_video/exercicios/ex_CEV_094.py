cadastro = dict()
dados = list()
media = 0

while True:
    cadastro['nome'] = input('Nome: ')
    cadastro['idade'] = int(input('Idade: '))
    media += cadastro['idade']
    cadastro['sexo'] = input('Sexo [M/F]: ')
    if cadastro['sexo'] not in 'MmFf':
        print('digite M- para Masculino ou F - para Feminimo!')
        cadastro['sexo'] = input('Sexo: ')

    dados.append(cadastro.copy())

    op = input('deseja continuar [S/N]: ')
    if op not in 'SsNn':
        op = input('Erro! digite S - para continuar ou N - para finalizar:  ')
    if op in 'Nn':
        break

print('-='*30)
print(f'ha {len(dados)} pessoas cadastradas')
print(f'a media de idade eh de {media/len(dados):5.2f} anos')
print(f'as mulheres cadastradas sao: ', end='')
for p in dados:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print(f'\n\nlista das pessoas acima da media: ')
for p in dados:
    if p['idade'] >= media/len(dados):
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}, ', end='')
        print()