nome = str(input('Digite seu nome: ')).strip()
print('nome : ',nome)
print('Maus. -> ', nome.upper())
print('Minus. -> ', nome.lower())
print('total de letras: ', len(nome) - nome.count(' '))
print('total de letras do 1º nome: ', nome.find(' '))

'''
separa = nome.split()
print('total de letras do 1º nome: ', len(separ[0]))
'''