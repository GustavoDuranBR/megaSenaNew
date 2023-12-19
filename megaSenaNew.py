import tkinter as tk
from tkinter import Scrollbar
from funcoesMegaSenaNew import *


class GeradorPalpitesMegaSena:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Palpites da Mega Sena")
        self.root.iconbitmap("D:\\PYTHON_PROJETOS\\megaSenaNew\\image\\trevo.ico")
        self.root.geometry("400x320")  # Tamanho inicial da janela

        self.label_num_jogos = tk.Label(root, text="Quantos jogos você quer gerar?")
        self.label_num_jogos.pack()

        self.entry_num_jogos = tk.Entry(root)
        self.entry_num_jogos.pack()

        self.btn_gerar = tk.Button(root, text="Gerar Palpites", command=self.exibir_palpite_gerado_wrapper)
        self.btn_gerar.pack()

        # Criação do Canvas e da Barra de Rolagem
        self.canvas = tk.Canvas(root)
        self.scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Frame interno ao Canvas
        self.frame_palpites = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_palpites, anchor="nw")

        self.frame_palpites.bind("<Configure>", lambda event: on_frame_configure(self.canvas, self.frame_palpites))

    def exibir_palpite_gerado_wrapper(self):
        exibir_palpite_gerado(self.entry_num_jogos, self.frame_palpites, gerar_palpite)


def main():
    root = tk.Tk()
    app = GeradorPalpitesMegaSena(root)
    root.mainloop()


if __name__ == "__main__":
    main()
