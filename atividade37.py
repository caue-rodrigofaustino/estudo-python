resposta = "Ss"
num = 0
maior = 0
menor = 0
total = 0
contagem = 0

while resposta not in "Nn":
    num = int(input("Digite um numero:"))
    contagem += 1
    total+= num

    if contagem == 1:
        menor = maior = num

    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resposta = str(input("Deseja continuar com adição de numeros?[S/N]").upper().strip()[0])
    
print(" ")
media = total / contagem
print(f"A media dos{contagem} numeros digitados foram {media}")
print(f"o maior numero dentre os digitados foi {maior}")
print(f"O menor numero digitado foi {menor}")