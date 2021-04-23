from random import *

print('$' * 27)
print('     Palpite MEGA-SENA     ')
print('$' * 27)


def contador(x):
    print(f'Os números da sorte são: \n{x}')
    print('$' * 30)


lista = []
lista2 = []
lista3 = []

for i in sample(range(1, 61), 6):
    lista.append(i)
contador(sorted(lista))

for i in sample(range(1, 61), 6):
    lista2.append(i)
contador(sorted(lista2))

for i in sample(range(1, 61), 6):
    lista3.append(i)
contador(sorted(lista3))

print('\n$$$ Boa sorte $$$')