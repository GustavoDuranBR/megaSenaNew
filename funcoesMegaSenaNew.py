from random import sample


def gerar_palpite():
    return sorted(sample(range(1, 61), 6))


def exibir_palpite(palpite):
    print(f'\n{palpite}')


def exibir_mensagem(msg):
    tam = len(msg) + 4
    print('$' * tam)
    print(f'  {msg}')
    print('$' * tam)