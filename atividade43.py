group_maior = 0
group_homens = 0
group_mulher = 0
encerrar = "resposta"

while encerrar != "n":
    repost = int(input("Digite sua idade"))
    sex = input("escolha o seu sexo: [M/F]").lower()

    if repost >= 18:
        group_maior +=1
    if sex == "h":
        group_homens += 1
    if repost < 20 and sex == "f":
        group_mulher += 1
    
    encerrar = input("Deseja continuar [S/N]").lower()

print(f"tem mais de 18 anos {group_maior} pessoas")
print(f"sexo masculino cadastradas foram {group_homens} pessoas")
print(f"sexo feiminino menor de 20 anos {group_mulher} pessoas")