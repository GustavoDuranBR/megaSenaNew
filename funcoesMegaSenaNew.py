from random import sample
import tkinter as tk


def gerar_palpite():
    return sorted(sample(range(1, 61), 6))


def on_frame_configure(canvas, frame):
    canvas.configure(scrollregion=canvas.bbox("all"))


def exibir_palpite_gerado(entry_num_jogos, frame_palpites, gerar_palpite):
    num_jogos = int(entry_num_jogos.get())
    palpites = []

    for _ in range(num_jogos):
        palpite = gerar_palpite()
        palpites.append(sorted(palpite))

    # Limpa a área de exibição de palpites
    for widget in frame_palpites.winfo_children():
        widget.destroy()

    # Exibe os palpites gerados
    for i, palpite in enumerate(palpites):
        texto_palpite = f"Palpite {i + 1}: {palpite}"
        label_palpite = tk.Label(frame_palpites, text=texto_palpite)
        label_palpite.pack()
