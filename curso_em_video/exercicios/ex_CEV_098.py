from time import sleep

def contagem(inicio, fim, intervalo):
    print('-='*30)
    print(f'contagem de {inicio} a {fim}, pulando de {intervalo}')
    sleep(2)

    #correcao de possiveis erro
    if intervalo < 0:
        intervalor *= -1 #isso pq nao existe intervalos negativo
    if intervalo == 0:
        intervalo = 1 # pq se o intervalo for zero a contagem fica parada

    #implementacao
    if inicio <= fim:
        c = inicio
        while c <= fim:
            print(f'{c} ',end='',flush=True) #correcando do erro na hora da impressao com o sleep, fazendo com que nao haja ligacao de buffer de tela.
            c += intervalo
            sleep(0.5)
        print('FIM')
    else:
        c = inicio
        while c >= fim:
            print(f'{c} ',end='',flush=True)
            sleep(0.5)
            c -= intervalo
        print('FIM')


#chamada da funcao
contagem(1, 10, 1)
contagem(10, 0, 2)
inic = int(input('digite um numero para ser o inicio: '))
f = int(input('digite um valor valor para ser o fim: '))
inter = int(input('digite um intervalo para a contagem: '))
contagem(inic, f, inter)
