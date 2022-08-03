import math
peso = float(input('peso: '))
altura = float(input('altura: '))
imc = (peso / math.pow(altura,2))
print('{:.2f}'.format(imc))
if imc < 18.5:
    print('abaixo de peso!')
elif 18.5 > imc <= 25:
    print('peso ideal!')
elif 25 > imc <= 30:
    print('acima do peso!')
elif 30 > imc <= 40:
    print('obesidade!')
else:
    print('obesidade morbida!')