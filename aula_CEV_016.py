'''
                    tuplas
-sao imutaveis!
'''

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
for comida in lanche:
    print(f'eu vou comer {comida}.')
print('eu comi muito!!!!')

print('segundo modo de fazer...')
#este pode mostrar a posiçao se voce colocar um {nome do laço}
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('eu comi muito!!!')
