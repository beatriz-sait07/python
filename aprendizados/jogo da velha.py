import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")
        
        self.tabuleiro = [" "]*9  
        self.jogador_atual = "O"  
        
        self.botoes = []
        
        for i in range(9):
            botao = tk.Button(self.janela, text=" ", font=("Arial", 20), height=4, width=8)
            botao.grid(row=i//3, column=i%3)
            botao.configure(command=lambda i=i: self.realizar_jogada(i))
            self.botoes.append(botao)
        
    def realizar_jogada(self, indice):
        if self.tabuleiro[indice] == " ":
            self.tabuleiro[indice] = self.jogador_atual
            self.botoes[indice].configure(text=self.jogador_atual)
            
            if self.verificar_vitoria(self.jogador_atual):
                messagebox.showinfo("FIM DE JOGO", f"O jogador {self.jogador_atual} venceu!")
                self.reiniciar_jogo()
            elif " " not in self.tabuleiro:
                messagebox.showinfo("FIM DE JOGO", "Empate!")
                self.reiniciar_jogo()
            else:
                self.jogador_atual = "X" if self.jogador_atual == "O" else "O"
    
    def verificar_vitoria(self, jogador):
        linhas = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        colunas = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]  
        diagonais = [[0, 4, 8], [2, 4, 6]]  
        
        for linha in linhas + colunas + diagonais:
            if all(self.tabuleiro[i] == jogador for i in linha):
                return True
        
        return False
    
    def reiniciar_jogo(self):
        self.tabuleiro = [" "]*9
        for botao in self.botoes:
            botao.configure(text=" ")
    
    def iniciar(self):
        self.janela.mainloop()

jogo = JogoDaVelha()
jogo.iniciar()
