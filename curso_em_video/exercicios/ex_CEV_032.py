from datetime import date
ano = int(input('digite 0 para analizar o ano ATUAL \nou digite o ano de sua preferencia: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} eh bissexto!'.format(ano))
else:
    print('o ano {} nao eh bissexto!'.format(ano))
