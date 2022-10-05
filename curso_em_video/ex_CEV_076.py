mercadorias = ('pao',0.25,
               'margarina', 6.75,
               'presunto', 16.90,
               'mussarela', 17.50,
               'ovos', 10.35)

print('-' * 30)
print('OFERTAS SEMANAIS^30')
print('-' * 30)

for prod in range(0, len(mercadorias)):
    if prod %2 == 0:
        print(f'{mercadorias[prod]:.<20}',end='')
    else:
        print(f'R$ {mercadorias[prod]:>5.2f}')
print('-'*50)
print('OFERTAS VALIDAS POR TEMPO DETERMINADO!^50')
print('-' * 50)
