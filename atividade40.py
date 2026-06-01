num = 0
continu = True

while continu:
    num = int(input("Digite um número para ver sua tabuada: "))
    cont = 1
    if num < 0:
        print("programa Calculadora encerrou!")
        break
    if num > 0:
        while cont <= 10:
            print(f"{num} x {cont} = {num * cont}")
            cont += 1
    
    