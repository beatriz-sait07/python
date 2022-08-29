cont = 's'
cont_idd = cont_sx = cont_mulher_menorIDD = 0
while True:
    nome = input('nome: ')
    idade = int(input('idade: '))
    sexo = input('sexo [M/F]: ').lower()[0]
    cont = input('deseja continuar [S/N]??  respo: ').lower()
    if cont != 's':
        break
    if idade >= 18:
        cont_idd += 1
    if sexo == 'm':
        cont_sx += 1
    if sexo == 'f' and idade < 20:
        cont_mulher_menorIDD += 1
print(f'ha {cont_mulher_menorIDD} mulheres com menos de 20 anos')
print(f'ha {cont_sx} homens cadastrados')
print(f'ha {cont_idd} pessoas com mais de 18 anos cadastradas')