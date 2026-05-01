respost = 'S'
maior = 0
menor = 0
media = 0
total = 0
contagem = 0

while respost in "Ss":
    entrada = int(input("digite um numero:"))
    total += entrada
    if contagem == 1:
        menor = entrada
        maior = entrada
    else:
        if entrada > maior:
            maior = entrada
        if entrada < menor:
            menor = entrada
    contagem += 1
    respost = str(input("Quer continuar?[S/N]").upper().strip()[0])

print("terminou")
media = total / contagem
print(f"media da soma total de numeros foi {media}")
print(f"o menor numero é {menor}")
print(f"o maior numero é {maior}")