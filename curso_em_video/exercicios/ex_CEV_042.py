l1 = float(input('1º lado: '))
l2 = float(input('2º lado: '))
l3 = float(input('base: '))
esc = l1 == l2

if (l1 + l2) >= 3:
    if l1 == l2 and l1 == l3:
        print('triangulo equilatero!')
    elif l1 == l2 and l1 != l3 or l1 == l2 and l2 != l3 or l3 == l1 and l3 != l2 or l3 == l2 and l3 != l1:
        print('triangulo isoceles!')
    else:
        print('triangulo escaleno')
else:
    print('nao forma um triangulo')


