sexo = input('qual seu sexo: [F/M]: ').strip().lower()[0]
while sexo not in 'MmFm':
    print('DADOS INVALIDOS!')
    sexo = str(input('INFORME SEU SEXO: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))


