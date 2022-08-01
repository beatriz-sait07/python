vel = flaot(input('velocidade: '))
if vel > 80:
    mult = 80
    print('voce foi multado no valor de R$ {:.2f}'.format(mult))
else:
    print('voce esta dentro da velocidade limite da pista!')
