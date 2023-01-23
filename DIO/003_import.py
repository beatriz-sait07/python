from A002c_funcoes import Tv
from A002b_funcoes import Calculadora
tv = Tv()
print(tv.ligada)
tv.power()
print(tv.ligada)

calc = Calculadora(5, 10)
print(calc.soma())