from time import sleep
from modularizacao import *
from utilizando_arq import *
arq = 'cursos.txt'

if not arqExiste(arq):
    criarArq(arq)

while True:
    resp = menu(['ver clientes cadastrados', 'cadastrar novo cliente', 'sair do programa'])
    if resp == 1:
        lerArq(arq)
    elif resp == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idd = leiaInt('IDADE: ')
        cadastrar(arq, nome, idd)
    elif resp == 3:
        sair()
        break
    else: 
        print('\033[31mErro: Digite um opcao valida!\033[m')
    sleep(1.2)
