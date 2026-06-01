import random

num = 0
tentativa = True
win = 0
loser = 0
comando = 1

while tentativa:
    while comando != 0:
        num = int(input("Digite um número: "))
        compiuter = random.randint(1,10)
        print(f"numero do computador {compiuter}")

        som = (num + compiuter) %2
        if som == 0:
            value = "par"
        else:
            value = "impar"
        
        chute = str(input("escolha se foi PAR ou IMPAR: ").lower())
        if chute == value:
            print("parabens você acertou!")
            tentativa = False
            win +=1
        elif chute != value:
            print("infelizmente você perdeu!")
            loser +=1
        else:
            print("ocorreu um erro insperado")
        comando = int(input("Digite 1 para continuar e 0 para encerrar: "))

print(f"o jogador teve um total de {win} vitorias e {loser} derrotas")
   


    

    
