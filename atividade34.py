primeiro_termo = int(input("digite um numero:"))
razao = int(input("digite a razão:"))
cont = 1
total = 0
mais = 10

while mais  !=  0:
    total = total + mais
    while cont <= total: 
        print(primeiro_termo,' -> ',end='')
        primeiro_termo += razao
        cont+=1
    print(" PAUSA ")
    mais = int(input("digite quantos numeros voce deseja imprimir novamente:"))
print("FIM")