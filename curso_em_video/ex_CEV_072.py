cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis','sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
dados = int(input('digite um numero de 0 - 20: '))
while True:
    print('voce digitou um numero invalido')
    tent = int(input('Digite novamente um numero entre 0 - 20: '))
    if 0 <= tent >= 20:
        break
print('\ndigito valido!\n')
print(cont[dados])

