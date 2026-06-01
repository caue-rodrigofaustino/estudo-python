while True:
    entrada_cpf = input("digite o numero do seu cpf: ")
    if len(entrada_cpf) == 11:
        break
    elif len(entrada_cpf) < 11:
        print("o numero atual esta menor que o exigido ")
print("cpf cadastrado com sucesso!")