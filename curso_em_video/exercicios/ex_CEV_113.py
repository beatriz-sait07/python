def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: entre com um valor inteiro valido!\033[m')
        else:
            return inteiro
        
def leiaFloat(msg):
    while True:
        try:
            real = float(input(msg))
        except (ValueError,  TypeError):
            print('\033[31mErro: Digite um valor real valido!\033[m')
        else:
            return float
        
        
intr = leiaInt('digite um valor inteiro:  ')
reais = leiaFloat('digite um valor real: ')