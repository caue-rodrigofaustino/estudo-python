valorone = int(input("Digite um primeiro valor:"))
valortwo = int(input("Digite um segundo valor:"))
n1 = valorone
n2 = valortwo

resultado = 0
escolha = "escolha"
maior = n1

while escolha != 5:
    print("ESCOLHA UMA OPERAÇÃO QUE DESEJA REALIZAR\n" \
    "1-SOMA\n2-MULTIPLICAÇÃO\n3-MAIOR NUMERO\n4-NOVOS NUMEROS\n5-SAIR")

    escolha = int(input("digite o numero que deseja escolhar:"))

    if escolha == 1:
        resultado = n1 + n2
        print(f"o valor da soma dois números é {resultado}")
    elif escolha == 2:
        resultado = n1* n2
        print(f"o valor da multiplicação dois números é {resultado}")
    elif escolha == 3:
        if maior < n2:
            maior = n2
        print(f"o valor maior entre os dois números é {maior}")
    elif escolha == 4:
        n1 = int(input("digite um novo número:"))
        n2 = int(input("digite um novo número:"))
    elif escolha == 5:
        print("programa encerrando.......")
        break
    else:
        print("erro ao escolher, tente novamente!")



