sex = 'sex'
resposta = 'resp'

while sex != 'M' and sex != 'F':
    sex = (input("digite seu sexo [M/F]:")).strip().upper()[0]
    if sex != 'M' and sex != 'F':
        while sex != "F" and sex != "M":
            sex = input("digite o sexo corretamente:").strip.upper()[0]
    if sex.upper() == "M" and sex == "F":
        break

print(f"SEXO {sex.upper()} REGISTRADO COM SUCESSO")