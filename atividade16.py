ld1 = float(input('digite um valor: '))
ld2 = float(input('digite um valor: '))
ld3 = float(input('digite um valor: '))

if ld1 < ld2 + ld3 and ld2 < ld1 + ld3 and ld3 < ld2 + ld1:
  if ld1 == ld2 == ld3:
     print('triangulo equilatero')
  elif ld1 == ld2 or ld1 == ld3 or ld3 == ld2:
     print('triangulo isoceles ')
  elif (ld1 != ld2) or (ld1 != ld3) or (ld3 != ld2):
     print('triangulo escaleno')