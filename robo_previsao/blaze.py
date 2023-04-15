# api blaze:  https://blaze.com/api/roulette_games/...

'''
cores:
0 -> branco
1 -> vermelho
2 -> preto
1 a 7 -> vermelhos
8 14 -> pretos
'''

import requests
from pprint import pprint #imprime as informacoes de forma mais organizada

requisicao = requests.get('https://blaze.com/api/roulette_games/recent').json() #joga dentro de uma variavel o json da requisição, ou seja,jogara as informacoes 

#crie uma lista com a cor e numero que saiu
giros = [[item['color'], item['roll']] for item in requisicao] #pra cada item de requisicao irei pegar a cor e o numero que foi sorteado pela roleta

#criando lista para dar as cores correspondentes com os numeros
info = []
for elemento in giros:
    if elemento[0] == 0:
        info.append(['write', 'black', elemento[1]]) #cor da caixa, cor do texto, local de armazenamento
    elif elemento[0] == 1:
        info.append(['red', 'write', elemento[1]])
    else:
        info.append(['black', 'write', elemento[1]])
        
pprint(info[:5])

#pprint(requisicao) #imprime o json
#print(requisicao[0]) -> imprime o primeiro jogo
#print(requisicao[0]['color']) -> imprime a cor do primeiro jogo