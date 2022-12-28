def jogador(jgd='<desconhecido>', gol=0):
        return f'o jogador {jgd} fez {gol} gol(s) no campeonato'

id = input('Nome do Jogador: ')
g = int(input('Quantidade de gols: '))
if id.strip() == '':
    print(jogador(gol=g))
else:
    print(jogador(id, g))