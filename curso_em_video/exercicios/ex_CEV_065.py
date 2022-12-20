opcao = 's'
soma = qnt = media = maior = menor = 0
while opcao in 's':
    n = int(input('Digite um valor: '))
    soma += n
    qnt += 1
    opcao = input('deseja continuar? [S/N]').lower()
    if qnt == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / qnt
print('numeros digiados: {}'.format(qnt))
print('media: {}'.format(media))
print('maior numero digitado: {}'.format(maior))
print('menor numeero digitado: {}'.format(menor))


