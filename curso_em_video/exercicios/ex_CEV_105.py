def notas(*num, sit=False):
    """ funcao para validacao de notas

    :para num: receba as notas
    :para sit:  valor opcional para aparicao de situacao do aluno
    :return: retorna um dicionario com os dados inserido
    """

    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num)/len(num)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        else:
            r['situacao'] = 'RUIM'
    return r

resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)