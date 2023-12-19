from funcoesMegaSenaNew import *

num_jogos = int(input('Quantos jogos você quer gerar? '))


def main():
    exibir_mensagem('Palpite MEGA-SENA')

    for jogo in range(num_jogos):
        palpite = gerar_palpite()
        exibir_palpite(palpite)


if __name__ == "__main__":
    main()
