#nesta atividade, eu criei um conversor de unidades
num = int(input('digite o numero: '))

#o numero digitado vai ser calculado por cada uma das variaveis
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#e sera mostrado o seu valor
print(f'unidade: {u}')
print(f'dezena: {d}')
print(f'centena: {c}')
print(f'milhar: {m}')