import random

pedra = 1
papel = 2
tesoura = 3

lista = [pedra, papel, tesoura]
print('1- pedra\n2- papel\n3- tesoura\nescolha um numero')
escolhido = random.choice(lista)
jog = int(input('escolha uma jogada'))


if jog == 1 and escolhido == 3 or jog == 2 and escolhido == 1 or jog == 3 and escolhido == 2:
  print('jogador ganhou do computador, párabens\n')
elif jog == escolhido:
  print('deu empate\n')
else:
  print('infelizmente voce nao venceu\n')

print('o jogador escolheu {}'.format(jog))
print('o computador escolheu {}'.format(escolhido))