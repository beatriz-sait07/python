#so ta funcionando no pycharm
from time import sleep
from modularizacao import *
from utilizando_arq import *

if not arqExiste('cursos.txt'):
    criarArq('cursos.txt')

while True:
    resp = menu(['ver clientes cadastrados', 'cadastrar novo cliente', 'sair do programa'])
    if resp == 1:
        lerArq('cursos.txt')
    elif resp == 2:
        cabecalho('OPCAO 2')
    elif resp == 3:
        sair()
        break
    else: 
        print('\033[31mErro: Digite um opcao valida!\033[m')
        sleep(2)