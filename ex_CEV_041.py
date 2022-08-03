from _datetime import date
nome = input('nome: ')
idade = int(input('ano de nascimento: '))
at = date.today().year
print(at - idade)
if (at - idade) <= 9:
    print('{} categoria mirim'.format(nome))
elif  9 > (at - idade ) <= 14:
    print('{} categoria infantil'.format(nome))
elif 14 > (at - idade ) <= 19:
    print('{} categoria junior'.format(nome))
elif 19 > (at - idade ) < 21:
    print('{} categoria senior'.format(nome))
else:
    print('{} categoria master'.format(nome))
