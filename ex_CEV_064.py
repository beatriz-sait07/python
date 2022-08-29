num = cont = soma = 0
num = int((input('Digite uma numero [999 - para a contagem]: ')))
while num != 999:
    soma += num
    cont += 1
    num = int((input('Digite uma numero [999 - para a contagem]: ')))
print('voce digitou {} numeros a soma deles foi de {}'.format(cont, soma))
