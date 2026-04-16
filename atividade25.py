from datetime import date

menor = 0
maior = 0
atual = date.today().year

for i in range(1, 7 + 1):
  nome = str(input("digite seu nome:"))
  ano = int(input("digite o ano de nascimento:"))
  sub = atual - ano

  if sub < 18:
    menor =  menor + 1
  elif sub >= 18:
    maior = maior + 1


print("=-=" * 10)
print("existem {} maiores de idade".format(maior))
print("existem {} menores de idade".format(menor))
print("=-=" * 10)
