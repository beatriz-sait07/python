def area(largura, comprimento):
    dados = largura * comprimento
    print(f'a Area total do terreno de {largura}X{comprimento} eh de {dados:.2f}m^2')


print('     Controle de Terrenos')
print('-'*30)
area((float(input('Largura (m): '))), (float(input('Comprimento (m): '))))
