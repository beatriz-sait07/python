# api blaze:  https://blaze.com/api/roulette_games/...

'''
ROBO QUE VAI ATE GALE 2!!

cores:
0 -> branco
1 -> vermelho
2 -> preto
1 a 7 -> vermelhos
8 14 -> pretos
'''

import requests
from pprint import pprint #imprime as informacoes de forma mais organizada
from tkinter import *

requisicao = requests.get('https://blaze.com/api/roulette_games/recent').json() #joga dentro de uma variavel o json da requisição, ou seja,jogara as informacoes 

def busca_giros():
    #crie uma lista com a cor e numero que saiu
    giros = [[item['color'], item['roll']] for item in requisicao][:6][::-1] #pra cada item de requisicao irei pegar a cor e o numero que foi sorteado pela roleta --- [:5] -> pega os 5 primeiros jogos --- [::-1] -> inverte a ordem da lista
    return giros
        
def return_color(giros):
#criando lista para dar as cores correspondentes com os numeros
    info = []
    for elemento in giros:
        if elemento[0] == 1:
            info.append(['red', '#FFDAB9', elemento[1]])
        elif elemento[0] == 2:
            info.append(['black', '#FFDAB9', elemento[1]])
        else:
            info.append(['write', '#FFDAB9', elemento[1]]) #cor da caixa, cor do texto, local de armazenamento
    return info
            
def atualizar():
    print('teste')
    dados_blaze = busca_giros()
    inf = return_color(dados_blaze)
    num0['text'] = inf[0][2]
    num1['text'] = inf[1][2]
    num2['text'] = inf[2][2]
    num3['text'] = inf[3][2]
    num4['text'] = inf[4][2]
    
    num0['bg'] = inf[0][0]
    num1['bg'] = inf[1][0]
    num2['bg'] = inf[2][0]
    num3['bg'] = inf[3][0]
    num4['bg'] = inf[4][0]
    
    #previsao sera feita atraves da suposicao que a soma dos valores sera par ou impar e a partir disto faremos a previsao se ele sera preto ou vermelho
    
    color_p = ''
    if sum([num[1] for num in dados_blaze]) % 2 == 0:
        color_p = 'black'
    else:
        color_p = 'red'
        
    prev = Label(height=2, width=96, bg=color_p)
    prev.grid(row=3, column=0, columnspan=5)

tela = Tk() #cria a tela
tela.resizable(False, False) #tela nao pode ser redimensionada
tela.title('Robo Blaze') #titulo da tela
#msg = Label(tela, text='teste', bg='red', fg='white') #cria uma label -> se houvesse mais de uma tela seria necessario colocar o nome da tela como parametro inicial
msg = Label(text = 'Giros Duble Blaze', bg='#FFDAB9', fg='#A52A2A', height=2, font = ('', 15), width=96)#txt da tela, cor de fundo, cor do texto, altura, estilo, tamanho da fonte e largura(esta sem nada nas '' pois esta usando a fonte padrao)
msg.grid(row=0, column=0, columnspan=5) #coloca a label na tela, lembrando que o grid eh um sistema parecido com o do excel, onde cada linha e coluna eh um numero, iremos deifinir isto dentro do parametro do grid -> parametro: row=linha, column=coluna, columnspan = meclar colunas

#colunas com as informacoes dos numeros que sairam
#define a caixa
num0 = Label(text='', bg='gray', fg='white', height=5, font = ('', 12), width=15)
num1 = Label(text='', bg='gray', fg='white', height=5, font = ('', 12), width=15)
num2 = Label(text='', bg='gray', fg='white', height=5, font = ('', 12), width=15)
num3 = Label(text='', bg='gray', fg='white', height=5, font = ('', 12), width=15)
num4 = Label(text='', bg='gray', fg='white', height=5, font = ('', 12), width=15)

#coloca a caixa na 'tela' com as definicoes de cor, tamanho e etc
num0.grid(row=1, column=0)
num1.grid(row=1, column=1)
num2.grid(row=1, column=2)
num3.grid(row=1, column=3)
num4.grid(row=1, column=4)

botao = Button(text= 'Atualizar', bg='#FFDAB9', fg='#A52A2A', height=2, font = ('', 15), width=96, command=lambda: atualizar()) #cria um botao -> text= texto do botao, bg=cor de fundo, fg=cor do texto, height=altura, font=estilo e tamanho da fonte, width=largura, command=funcao que sera executada quando o botao for clicado
botao.grid(row=2, column=0, columnspan=5) #coloca o botao na tela
 
tela.mainloop() #loop da tela

#pprint(requisicao) #imprime o json
#print(requisicao[0]) -> imprime o primeiro jogo
#print(requisicao[0]['color']) -> imprime a cor do primeiro jogo