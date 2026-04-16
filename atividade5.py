import random
#importei uma bliblioteca para conseguir utilizar seus metodos

print('-' * 7,  'DESCUBRA O NUMERO SECRETO', '-' * 7 )

#utilizo randint para sortear um numero aleatorio, que colocamos como argumento entre os parenteses
n = random.randint(0,9 + 1)
c = int(input('digite seu numero de chute:ex:1 a 9 '))

#utilizei condicional para
if c >= 9 and c <= 1:
  print("erro, digite um numero valido")
else:
   if c == n:
     print('parabens, ACERTOUU!')
   else:
     print('ERROU, FOI QUASE!')