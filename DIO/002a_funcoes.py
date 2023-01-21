'''
no python nao tem essa diferenciacao explicita!  -> def

metodo: tudo que nao retorna um valor     
funcoes: tudo que retorna um valor
'''
def soma(a=0, b=0):
    return a + b

def subt(a=0, b=0):
    return a - b

def mult(a=0, b=0):
    return a * b

def div(a=0, b=0):
    return a / b

print(soma(3,4))
print(f'usando DEF:  a=4, b=2\nsoma: {soma(4, 2)}\nsubtracao: {subt(4, 2)},\nmultiplicacao: {mult(4, 2)}\ndivisao: {div(4, 2)}')



class Calculadora:
    def __init__(self, a, b):
        self.valor_a = a
        self.valor_b = b
    def soma1(self):
        return self.valor_a + self.valor_b

    def subt1(self):
        return self.valor_a - self.valor_b

    def mult1(self):
        return self.valor_a * self.valor_b

    def div1(self):
        return self.valor_a / self.valor_b
    
print('\n\nusando CLASSE:    a=4, b=2')
calculadora_main = Calculadora(4, 2)
print(f'soma: {calculadora_main.soma1()}\nsubtracao: {calculadora_main.subt1()},\nmultiplicacao: {calculadora_main.mult1()}\ndivisao: {calculadora_main.div1()}')