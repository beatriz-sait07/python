coloc = ('palmeiras', 'flamengo', 'fluminense', 'corinthians',
         'internacional', 'athletico-pr', 'atletico-ms', 'santos'
         'americas-mg', 'goias', 'red bull', 'fortaleza', 'sao paulo',
         'botafogo', 'ceara', 'curitiba', 'cuiaba', 'avai', 'atletico-go', 'juventude')
print(f'os cinco primeiros colocados: {coloc[:6]}')
print(f'os 4 ultimos colocados: {coloc[15:]}')
print(f'os times em ordem alfabetica: ', sorted(coloc))
print(f'o red bull encontra-se na posicao: ', coloc.index('red bull'))
