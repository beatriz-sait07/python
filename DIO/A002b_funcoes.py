class Calculadora:
    def __init__(self):
        pass #nao faz nada, apenas um comando para deixar o init vazio   ou faz sem o init

    def soma1(self, valor_a, valor_b):
        return valor_a + valor_b

    def subt1(self, valor_a, valor_b):
        return valor_a - valor_b

    def mult1(self, valor_a, valor_b):
        return valor_a * valor_b

    def div1(self, valor_a, valor_b):
        return valor_a / valor_b
    
print('\n\nusando CLASSE:    a=4, b=2')
calculadora_main = Calculadora()
print(f'soma: {calculadora_main.soma1(4,2)}\nsubtracao: {calculadora_main.subt1(4,2)},\nmultiplicacao: {calculadora_main.mult1(4,2)}\ndivisao: {calculadora_main.div1(4,2)}')