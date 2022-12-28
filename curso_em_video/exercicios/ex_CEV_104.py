def validacao_int(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO!  Digite um numero inteiro valido ')
        if ok:
            break
        
    return valor

n = validacao_int('digite um valor: ')
print(f'voce acabou de digitar o numero {n}')