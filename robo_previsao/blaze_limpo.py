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
from tkinter import *

#requisicao = requests.get('https://blaze.com/api/roulette_games/recent').json()

def busca_giros():
    giros = [[item['color'], item['roll']] for item in requests.get('https://blaze.com/api/roulette_games/recent').json()][:5][::-1]
    return giros
        
def return_color(giros):
    info = []
    for elemento in giros:
        if elemento[0] == 1:
            info.append(['red', '#FFDAB9', elemento[1]])
        elif elemento[0] == 2:
            info.append(['black', '#FFDAB9', elemento[1]])
        else:
            info.append(['white', '#FFDAB9', elemento[1]])
    return info

def atualizar_com_atraso():
    tela.after(1000, atualizar)

            
def atualizar():
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
    
    color_p = ''
    if sum([num[1] for num in dados_blaze]) % 2 == 0:
        color_p = 'black'
    else:
        color_p = 'red'
        
    prev = Label(height=2, width=96, bg=color_p)
    prev.grid(row=3, column=0, columnspan=5)
    #tela.after(1000, atualizar)
    

tela = Tk()
tela.resizable(False, False) 
tela.title('Robo Blaze')
msg = Label(text = 'Giros Duble Blaze', bg='#FFDAB9', fg='#A52A2A', height=2, font = ('', 15), width=96)
msg.grid(row=0, column=0, columnspan=5)

num0 = Label(text='', bg='gray', fg='white', height=5, font = ('', 12), width=15)
num1 = Label(text='', bg='gray', fg='white', height=5, font = ('', 12), width=15)
num2 = Label(text='', bg='gray', fg='white', height=5, font = ('', 12), width=15)
num3 = Label(text='', bg='gray', fg='white', height=5, font = ('', 12), width=15)
num4 = Label(text='', bg='gray', fg='white', height=5, font = ('', 12), width=15)

num0.grid(row=1, column=0)
num1.grid(row=1, column=1)
num2.grid(row=1, column=2)
num3.grid(row=1, column=3)
num4.grid(row=1, column=4)

botao = Button(text= 'Atualizar', bg='#FFDAB9', fg='#A52A2A', height=2, font = ('', 15), width=96, command=lambda: atualizar())
botao.grid(row=2, column=0, columnspan=5)
 
tela.mainloop()