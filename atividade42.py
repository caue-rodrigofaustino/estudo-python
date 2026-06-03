import random

num = 0
tentativa = True
win = 0
loser = 0
comando = 1

while comando != 0:
    num = int(input("Digite um número: "))
    compiuter = random.randint(1,10)
    print(f"numero do computador {compiuter}")

    som = (num + compiuter) %2
    if som == 0:
        value = "p"
    else:
        value = "i"
        
    chute = str(input("escolha [P/I]: ").lower())
    if chute == value:
        print("parabens você acertou!")
        tentativa = False
        win +=1
    elif chute != value:
        print("infelizmente você perdeu!")
        loser +=1
        break
    else:
        print("ocorreu um erro insperado")

print(f"o jogador teve um total de {win} vitorias e {loser} derrotas")
   


    

    
