dados = dict()
gol = list()
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'quantas partidas {dados["nome"]} jogou: '))

for c in range(partidas):
    gol.append(int(input(f'quantos gols {dados["nome"]} fez na partida {c+1}: ')))
dados['gols'] = gol
dados['total'] = sum(gol) #soma os dados de dentro de uma lista

#prints
print('-'*30)
print(dados)
print('-'*30)
print()

for k, v in dados.items():
    print(f'o campo {k} tem o valor {v}.')
print('-'*30)
print(f'o jogador {dados["nome"]} jogou {partidas} partidas.')

for i, v in enumerate(dados["gols"]):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'foi um total de {dados["total"]} gols')

