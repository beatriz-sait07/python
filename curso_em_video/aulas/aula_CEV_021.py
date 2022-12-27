#--------------------aula teorica----------------------------
#declaracao de funcoes
def contador(i, f, p):
    # docstrings, serve como 'manual de instrucoes' da sua funcao.
    """
    --> Faz uma contagem e mostra na tela.
    :para i: insira um inicio da contagem
    :para f: insira um fim da contagem
    :para p: insira um intervalo para a contagem
    :return: sem retorno

    funcao criada por Beatriz Saito, usando dados do Gustavo Guanabara
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c+= p
    print('FIM')

contador(2, 10, 2)
#help(contador)
print('\n\n')
print('-='*30)
###############################################################
# funcao com parametro opcional
def somar(a=0, b=0, c=0):
    """
    --> realiza a somatoria de tres valores e imprime seu resultado
    :para a: o primeiro valor
    :para b: o segundo valor
    :para c: o terceiro valor
    :para s: somatoria de a+b+c
    :return: inexistente

    funcao criada por Beatriz Saito
    """
    s = a + b + c
    print(f'a soma vale {s}')


somar(5, 5, 1)
somar(1, 2)
somar(2)
#help(somar)
print('\n\n')
print('-='*30)
########################################## 
#escopo de variaveis
def teste():
    x = 8 # escopo local, so funciona na funcao ou local que foi criado
    print(f'na funcao teste, n vale {n}')
    print(f'na funcao teste, x vale {x}')

n = 2 #escopo global
print(f'no programa principal, n vale {n}')
teste()
# print(f'no programa principal, x vale {x}')

print('\n\n')
print('-='*30)
########################################## 
# funcao com return
def somar_return(a=0, b=0, c=0):
    s = a+b+c
    return s

resp = somar_return(3, 2, 5)
print(f'usando uma variavel: {resp}')
print(f'usando a propria funcao: {somar_return(3, 2, 5)}')

r1 = somar_return(1, 7)
r2 = somar_return(4)
print(f' meus calculos foram: {resp}, {r1} e {r2}')

print('\n\n')
print('~'*70)
########################################## 
# mostrando diferenca entre variavel globa e local
def test(b):
    a = 8 #usa este a dentro da funcao sem interferencia do 'a' global
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
test(a)
print(f'A fora vale {a}')

print('\n\n')
print('-='*30)
########################################## 
# substituindo variavel global, pela variavel local
def test1(b):
    global a 
    a = 8 #passa a usar este 'a' como substituto do 'a' global, apenas por chamar 'global' acima
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
print(f'antes de chamar a funcao:\nA fora vale {a}')
test1(a)
print(f'apos chamar a funcao:\nA fora vale {a}')
test1(a)

print('\n\n')
print('.^.'*30)
#--------------------aula pratica----------------------------
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('digite um numero: '))
print(f'o fatorial de {n} eh: {fatorial(n)}')


print('\n\n')
print('-='*30)
#################################################
def par_impar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('digite um valor: '))
if par_impar(num):
    print('par')
else:
    print('impar')