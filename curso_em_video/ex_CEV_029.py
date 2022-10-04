vel = float(input('velocidade: '))
if vel > 80:
    mult =(vel - 80) * 7
    print('voce foi multado no valor de R$ {:.2f}'.format(mult))
else:
    print('voce esta dentro da velocidade limite da pista!')
