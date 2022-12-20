salario = float(input('qual seu salario ? '))
if salario > 1.250:
    print('R$ {:.2f}'.format(salario + (10/100 * salario)))
    print('este eh seu salario com aumento de 10%')
else:
    print('R$ {:.2f}' .format(salario + (15/100 * salario)))
    print('este eh seu salario com aumento de 15%')
