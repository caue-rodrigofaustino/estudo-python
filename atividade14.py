a = int(input('digite um numero: '))
b = int(input('digite um numero: '))
c = int(input('digite um numero: '))

menor = a
if b < a and b < c:
 menor = b
if c < a and c < b:
  menor = c

maior = a
if b >  a and b > c:
  maior = b

if c > a and c > b:
  maior = c
print('\033[33mmaior {} \033[m \nmenor \033[432m{} \033[m'.format(maior,menor))