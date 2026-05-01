primeiro_termo = int(input("digite um numero:"))
razao = int(input("digite a razão:"))
numeros = 1

while numeros < 11:
    print(primeiro_termo,",", end='')
    primeiro_termo += razao
    numeros += 1