nome = input('qual seu nome: ')
n1 = float(input('1º nota: '))
n2 = float(input('2º nota: '))
media = (n1 + n2) / 2
print('sua media eh: {}'.format(media))
if media < 5:
    print('{} esta \033[1;31mREPROVADO\033[m'.format(nome))
elif 5 > media < 6.9:
    print('{} esta de \033[1;33mRECUPERACAO\033[m'.format(nome))
else:
    print('{} esta \033[1;32mAPROVADO\033[m'.format(nome))
