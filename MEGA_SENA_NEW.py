from random import *


def texto(msg):
    tam = len(msg) + 4
    print('$' * tam)
    print(f'  {msg}')
    print('$' * tam)



def contador(x):
    print(f'\n{x}')



lista = []
lista2 = []
lista3 = []

texto('Palpite MEGA-SENA')

for i in sample(range(1, 61), 6):
    lista.append(i)
contador(sorted(lista))

for i in sample(range(1, 61), 6):
    lista2.append(i)
contador(sorted(lista2))

for i in sample(range(1, 61), 6):
    lista3.append(i)
contador(sorted(lista3))

