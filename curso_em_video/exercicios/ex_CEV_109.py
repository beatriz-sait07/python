from modularizacao import moeda,metade,dobro,diminuir,aumento

valor = float(input('Digite um valor: '))
print(f'a metade de R$ {moeda(valor)} eh R$ {metade(valor, True)}')
print(f'o dobro de R$ {moeda(valor)} eh de {dobro(valor, True)}')
print(f'aumentando 10%, em R$ {moeda(valor)} teremos R$ {aumento(valor,10, True)}')
print(f'desconto de 10%, em R$ {moeda(valor)} teremos R$ {diminuir(valor,10, True)}')