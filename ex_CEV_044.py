preco = float(input('qual o preco da mercadoria:\nR$ '))
fp = input('formas de pagamento:\n1)a vista - dinheiro\n2)cartao debito\n3)credito - ate 2x\n4)credito - mais 3x \nescolha: ')
if fp == '1':
    print('R$ {:.2f} com desconto de 10%'.format(preco - (10/100 * preco)))
elif fp == '2':
    print('R$ {:.2f} com desconto de 5%'.format(preco - (5/100 * preco)))
elif fp == '3':
    print('R$ {:.2f} a mercadoria nao tem desconto'.format(preco))
elif fp == '4':
    print('R$ {:.2f} a mercadoria contem juros de 20%'.format(preco + (20/100 * preco)))
else:
    print('numero invalido!')
    print('------programa finalizado-----')
