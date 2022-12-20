print('-' * 30)
print('buscando vogais')
print('-' * 30)
palavras = ('amor',
            'futuro', 'carinho', 'estudos', 'praticas', 'paralelepipodo')
for vogais in palavras:
    print(f'\n{vogais.upper()} -> ',end='')
    for letras in vogais:
        if letras in 'aeiou':
            print(letras, end='')
print('\n\n')
