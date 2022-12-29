import modularizacao

valor = float(input('Digite um valor: '))
print(f'a metade de R$ {valor} eh R$ {modularizacao.metade(valor)}')
print(f'o dobro de R$ {valor} eh de {modularizacao.dobro(valor)}')
print(f'aumentando 10%, em R$ {valor} teremos R$ {modularizacao.aumento(valor)}')