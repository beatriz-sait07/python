class Fila:
    def __init__(self) -> None:
        self.fila = []
    
    def entrar(self, nome):
        self.fila.append(nome)
    def sair(self):
        if(len(self.fila) > 0):
            self.fila.pop(0)
        else:
            print("A fila está vazia")
            
#minuto :