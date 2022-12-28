def fatorial(num, show=False):
    """
    -> calcula o fatorial de um numero
    :para n: numero para saber o fatorial
    :para show: mostra o passo a passo seguido para a resposta
    :return: retorna o resultado
    """
    cont = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        cont *= c
    return cont

n = int(input('digite um numero: '))
print(f'o fatorial de {n} eh: {fatorial(n)}')
print(fatorial(n, show=True))