def lin():
    print('-'*30)

def mensagem(msg):
    print('-'*30)
    print(msg)


# PARTE TEORICA DA AULA
#programa principal
print('METODO USADO ATE AGORA!')
print('-'*30)
print(' curso em video')
print('-'*30)
print(' aprenda python')
print('-'*30)
print(' Gustavo Guanabara')
print('-'*30)
#------------------------------------
print('\n\nMETODO USANDO FUNCOES...')
lin()
print(' curso em video')
lin()
print(' aprenda python')
lin()
print(' Gustavo Guanabara')
lin()
#------------------------------------
print('\n\nMETODO USANDO FUNCOES COM PARAMETRO...')
mensagem(' curso em video')
mensagem(' aprenda python')
mensagem(' Gustavo Guanabara')
lin()
#=====================================
# PARTE PRATICA
def soma(x, y):
    print(f'X = {x} e Y = {y}')
    s = x + y
    print(f'a soma de {x}+{y} = {s}\n')

print('\n\naula pratica:')
soma(4, 5)
soma(x=5, y=2)
soma(y=2, x=4)
lin()

def contador(* num):
    print(num)

contador(2, 1, 7)
contador(0, 3)
contador(8, 9, 16, 12, 0, 3)


def dobra(lista):
    pos = 0#posicao
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


lin()
valores = [2, 4, 6, 8]
print(f'lista original: {valores}')
dobra(valores)
print(f'lista modificada: {valores}')