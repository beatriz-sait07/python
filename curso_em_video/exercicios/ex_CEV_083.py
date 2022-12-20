conta = input('Digite a expressao: ')
pilha = []
for simb in conta:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            #remove o ultimo elemento
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('expressao valida!')
else:
    print('expressao invalida!')
    
'''criou uma pilha aux para receber o par de parentese'''