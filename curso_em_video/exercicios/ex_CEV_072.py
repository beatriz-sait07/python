cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis','sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
        num = int(input('Digite um numero entre 0 - 20: '))
        if 0 <= num <= 20:
                print(f'voce digitou o numero {cont[num]}')
        if( 0 < num >= 21):
                print('tente novamente...', end='')
                num = int(input('Digite um numero entre 0 - 20: '))
        if num == 000:
                print('voce digitou "000" isso encerra o programa!')
                break
print('obrigada por sua cooperacao!')