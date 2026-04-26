import random

num = random.randint(1,10 + 1)
resposta = 0
palpite = 0
while resposta != num:
    resposta = int(input("digite seu chute:"))
    palpite += 1
print("parabéns voce acertou")
print("precisou de {} palpites para acertar".format(palpite))