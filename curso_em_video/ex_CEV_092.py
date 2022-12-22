from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['dn'] = datetime.now().year - nasc
opc = int(input('Carteira de trabalho (0 - caso nao tenha)'))
if(opc == 0):
    print('-='*30)
    print(f'nome: {dados["nome"]}\nIdade: {dados["dn"]}\nctps: nao tem\n')
else:
    dados['cdt'] = opc
    dados['contratacao'] = int(input('ano de contratacao: '))
    dados['salario'] = float(input('Salario:   R$ '))
    dados['aposentadoria'] = (dados['dn'] + (dados['contratacao'] + 35) - datetime.now().year)
    if dados['contratacao'] < dados['dn']:
        dados['contratacao'] = 'o ano de contratacao nao condiz com uma epoca existente de sua vida!'
    print('-='*30)
    print(f'nome: {dados["nome"]}\nIdade: {2022 - dados["dn"]}\nCTPS: {dados["cdt"]}')
    print(f'Ano de contratacao: {dados["contratacao"]}\nSalario:   R$ {dados["salario"]}')
    print(f'Aposentara com {dados["aposentadoria"]}')