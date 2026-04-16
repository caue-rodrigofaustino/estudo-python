import time
#para essa atividade, organizei uma estrutura que recebe tres valores
ld1 = int(input('digite o primeiro lado: '))
ld2 = int(input('digite o segundo lado: '))
ld3 = int(input('digite o terceiro lado: '))
print('Carregando...')
time.sleep(3)

#utilizei a estrutura if else para mostra um print, caso os lados consigam fazer um triangulo ou nao
if ld1 < ld2 + ld3 and ld2 < ld3 + ld1  and ld3 < ld1 + ld2:
  print('pode formar um triangulo')
else:
  print('nao pode formar um triangulo')