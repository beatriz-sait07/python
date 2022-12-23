dados = dict()
gol = list()
time = list()

while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'quantas partidas {dados["nome"]} jogou: '))
    gol.clear()

    for c in range(partidas):
        gol.append(int(input(f'quantos gols {dados["nome"]} fez na partida {c+1}: ')))
    dados['gols'] = gol[:]
    dados['total'] = sum(gol) #soma os dados de dentro de uma lista
    time.append(dados.copy())

    while True:
        resp = input('deseja continuar [S/N]?  ')
        if resp in 'SsNn':
            break
        print('Erro: responda apenas com S/N: ')
    if resp in 'Nn':
        break

print('-'*70)
print('cod  ',end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*70)     
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('mostrar os dados de qual jogador?  (999 - finaliza)'))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro: nao existe um jogador com este codigo de busca!')
    else:
        print(f' -- dados do jogador {time[busca]["nome"]}')
        for ind, gol in enumerate(time[busca]['gols']):
            print(f'     no jogo {ind+1} fez {gol} gols')
print('-'*70)