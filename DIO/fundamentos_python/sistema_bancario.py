valor_em_conta = 0.0
saque = 0.0
deposito = 0.0
cont_saque = 0
while True:
    opcao = input('''qual operacao deseja realizar ?\n[D] deposito\n[S] saque\n[E] extrato\n[Q] sair/quit\n''').upper()
    print('-'*45)
    
    if opcao == 'D':
        deposito = float(input('valor que deseja depositar: R$ '))
        print('-'*45)
        valor_em_conta = valor_em_conta + deposito
    
    elif opcao == 'S':
        saque = float(input('valor que deseja sacar: R$ '))
        if saque > 500:
            print('ERRO!! saque apenas abaixo de R$ 500.00\n')
            print('-'*45)
            continue
        elif saque > valor_em_conta:
            print('valor indiponivel para saque!\n')
            print('-'*45)
        else:
            cont_saque += 1
            if cont_saque > 3:
                print('ERRO! limite de quantidade de saque diario atingido!')
                print('-'*45)
                continue
            valor_em_conta  = valor_em_conta - saque
        
    elif opcao == 'E':
        print(f'Depósito: {deposito:>20.2f}')
        print(f'Saque: {saque:>23.2f}')
        print(f'Total em conta: {valor_em_conta:>14.2f}')

        
    elif opcao == 'Q':
        break
    else:
        print('Por gentileza, digite uma opcao valida!')
        continue
