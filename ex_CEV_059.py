n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
opcao = 0

while opcao != 5:
    print('''[1] somar
[2] multiplicar
[3] maior'
[4] novos numeros
[5] sair\n''')
    print('**************************************')
    opcao = int(input('>>>>> qual sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('SOMA -> {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('MULTIPLICACAO -> {} x {} = {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('o maior numero entre {} e {} eh {}'.format(n1, n2, maior))

    elif opcao == 4:
        n1 = int(input('1º novo numero: '))
        n2 = int(input('2ºnovo numero: '))
    elif opcao == 5:
        print('finalizando...')
    else:
        print('numero invalido!\nQual sua opçao?')

print('fim')