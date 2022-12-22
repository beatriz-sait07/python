estudantes = {'nome': input('nome do aluno: '), 'nota': float(input('nota: '))}
print('-='*30)

if estudantes['nota'] <= 5:
    print(f'Nome: {estudantes["nome"]}\nMedia: {estudantes["nota"]}\nSituacao: Reprovado\n')
elif estudantes['nota'] > 5 and estudantes['nota'] < 7:
    print(f'Nome: {estudantes["nome"]}\nMedia: {estudantes["nota"]}\nSituacao: Exame, precisando de {7 - estudantes["nota"]}\n')
else:
    print(f'Nome: {estudantes["nome"]}\nMedia: {estudantes["nota"]}\nSituacao: Aprovado\n')