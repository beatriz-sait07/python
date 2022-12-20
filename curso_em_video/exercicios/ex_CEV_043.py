import math
peso = float(input('peso: '))
altura = float(input('altura: '))
imc = (peso / math.pow(altura,2))
print('{:.2f}'.format(imc))
if imc <=  18.5:
    print('abaixo de peso!')
elif imc <= 25:
    print('peso ideal!')
elif imc <= 30:
    print('acima do peso!')
elif imc <= 40:
    print('obesidade!')
else:
    print('obesidade morbida!')