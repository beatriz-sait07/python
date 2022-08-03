from datetime import date
atual = date.today().year
nome = input('qual seu nome: ')
idade = int(input('informe sua ano de nascimento: '))
if (atual - idade) == 18:
    print('voce tem que se aistar imadiatamente!')
elif (atual - idade) < 18:
    alist = 18 - (atual - idade)
    print('falta {} anos para voce se alistar'.format(alist))
else:
    alist = (atual - idade) - 18
    print('voce devia ter se alistado ha {} anos'.format(alist))
