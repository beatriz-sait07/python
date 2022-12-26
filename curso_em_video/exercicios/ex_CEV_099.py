from time import sleep

def maior(* num):
    cont = maior = 0
    print('-='*30)
    print('\nanalisando valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.25)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'\no maior valor da lista acima eh {maior}')


maior(2, 9, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()