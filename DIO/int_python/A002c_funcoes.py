class Tv:
    def __init__(self):
        self.ligada = False
        self.channel = 3
    
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True
            
    def next_channel(self):
        self.channel += 1
        
    def prev_channel(self):
        self.channel -= 1
        

if __name__ == '__main__':  #imprime tudo que esta na 'main' se for dentro DESTE arquivo, caso voce importe este arquivo o texto da main nao aparecera no arquivo que recebera o import
    tv_main = Tv()
    print(f'a tv esta ligada: {tv_main.ligada}')
    tv_main.power()
    print(f'a tv esta ligada: {tv_main.ligada}')
    tv_main.power()
    print(f'a tv esta ligada: {tv_main.ligada}')
    print(f'canal: {tv_main.channel}')
    tv_main.next_channel()
    tv_main.next_channel()
    print(f'canal: {tv_main.channel}')
    tv_main.prev_channel()
    print(f'canal: {tv_main.channel}')
