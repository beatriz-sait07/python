valor_casa = float(input('valor da casa: '))
salario = float(input('salario: '))
tempo = int(input('pretende quitar a casa em quanto tempo (anos): '))
mensalidade = valor_casa / (tempo * 12)
print('R$ {:.2f} por mes'.format(mensalidade))
if mensalidade < (salario - (30/100 * salario)):
    print('emprestimo \033[1;32mAPROVADO\033[m')
else:
    print('emprestimo \033[1;31mNEGADO\033[m')