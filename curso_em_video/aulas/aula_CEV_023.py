#aula teorica
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'problema detectado {erro.__class__}(')
else:
    print(f'o resultado eh {r}')
    
finally:
    print('volte sempre! Muito obrigada!')