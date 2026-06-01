contador = 0
num = 0
soma = 0

while num != 999:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    soma = soma + num
    print(f"{soma}")
    contador =+ 1

print(f"o valor da soma foi {soma}")
    