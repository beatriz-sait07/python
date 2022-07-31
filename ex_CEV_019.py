import random
al = input('1º aluno: ')
al1 = input('2º aluno: ')
al2 = input('3º aluno ')
al3 = input('4º aluno: ')
lista = [al, al1, al2, al3]
es = random.choice(lista)
print('o aluno {} apagara o quadro'.format(es))
