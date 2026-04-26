sex = 'sexo'
while sex != 'M' and sex != 'F':
    sex = str(input("digite seu sexo M/F:")).upper()
    while sex != 'M' and sex != 'F':
        print("digite o sexo corretamente")
        sex = str(input("digite seu sexo M/F:")).upper()
   
