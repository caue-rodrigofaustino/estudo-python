total = int(input("digite quantos numeros de fibonati deseja mostrar:"))
anterior = 0
atual = 1
mais = 0

print("{} -> {}".format(anterior, atual), end="")
cont = 3

while total != 0:
    total = total + mais
    while cont <= total:
        proximo = anterior + atual
        print("-> {}".format(proximo), end="")
        anterior = atual
        atual = proximo
        cont+=1
    print(" -> pausa")
    mais = int(input("digite quantos numeros deseja ver:"))
    

    

