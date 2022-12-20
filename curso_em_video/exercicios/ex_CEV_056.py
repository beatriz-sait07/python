soma_idade = 0
media_idade = 0
mulher_menor = 0
nome_velho = ''
velho = 0
for dados in range(1, 5):
    print('---------------{} pessoa--------------'.format(dados))
    nome = input('nome: ').strip()
    idade = int(input('idade: '))
    sexo = input('seco [F/M]: ').strip()
    soma_idade += idade
    if dados == 1 and sexo in 'Mm':
        velho = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_menor += 1
media_idade = soma_idade / 4
print('a idade media da turma eh de {} anos'.format(media_idade))
print('o {} eh a pessoa mais velha entre os homens, tendo {} anos'.format(nome,idade))
print('ao todo sao {} mulheres menores de 20 anos'.format(mulher_menor))

