def idade(idd):
    from datetime import datetime
    idd1 = datetime.now().year - idd
    if idd1 < 16:
        return f'com {idd1}: NAO PODE VOTAR'
    elif 16 >= idd1 < 16 or idd >= 65:
        return f'com {idd1}: VOTO OPCIONAL'
    else:
        return f'com {idd1}: VOTO OBRIGATORIO'

nsc = int(input('Em que ano voce nasceu? '))
print(idade(nsc))