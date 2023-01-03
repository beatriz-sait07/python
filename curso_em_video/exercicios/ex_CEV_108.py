import modularizacao

valor = float(input('Digite um valor: '))
print(f'a metade de R$ {modularizacao.moeda(valor)} eh R$ {modularizacao.moeda(modularizacao.metade(valor))}')
print(f'o dobro de R$ {modularizacao.moeda(valor)} eh de {modularizacao.moeda(modularizacao.dobro(valor))}')
print(f'aumentando 10%, em R$ {modularizacao.moeda(valor)} teremos R$ {modularizacao.moeda(modularizacao.aumento(valor, 10))}')
print(f'desconto de 10%, em R$ {modularizacao.moeda(valor)} teremos R$ {modularizacao.moeda(modularizacao.diminuir(valor, 10))}')