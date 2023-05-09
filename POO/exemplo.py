from abstracao_de_dados import Fila

supermercado = Fila()
loterica = Fila()
banco = Fila()

supermercado.entrar("João")
supermercado.entrar("Maria")
supermercado.entrar("José")
loterica.entrar("Duda")
banco.entrar("Jhow")
banco.entrar("Susy")
banco.entrar("Bia")


print("Ao entrar\nFila do supermercado:" , supermercado.fila)
print("Fila da lotérica:" , loterica.fila)
print("Fila do banco:" , banco.fila)

supermercado.sair()
banco.sair()
loterica.sair()

print("\n\nPessoas foram atendidas\nFila do supermercado:" , supermercado.fila)
print("Fila da lotérica:" , loterica.fila)
print("Fila do banco:" , banco.fila)