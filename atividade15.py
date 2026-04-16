import random
alun1 = str(input('digite seu nome:'))
alun2 = str(input('digite seu nome:'))
alun3 = str(input('digite seu nome:'))

lista = [alun1, alun2, alun3]
random.shuffle(lista)
print('\033[1;34;40mescolha: {}\033[m'.format(lista))