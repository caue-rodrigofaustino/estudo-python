num = 0
contagem = 0
escolha = 0

while escolha != 999:
    escolha = int(input("digite um numero [999 interrompe o programa]:").strip())
    if escolha != 999:
        num += escolha
    elif escolha == 999:
        break
    contagem += 1

print(f"Você digitou {contagem} vezes antes de sair do loop")
print(f"a soma dos numeros digitados foi {num}")