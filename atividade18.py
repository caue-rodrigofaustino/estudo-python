peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))

imc = peso / (altura **2)

if imc < 18.5:
  print('{:.2f} baixo peso, busque aumentar sua massa muscular'.format(imc))
elif imc >= 18.5 and imc < 25:
  print('{:.2f} peso ideal para voce '.format(imc))
elif imc >= 25 and imc <  30:
  print('sobrepesso {:.2f}. ta virando um leitao'.format(imc))
elif imc >= 30 and imc < 40:
  print('obessidade {:.2f}. busque emagrecer porquinho'.format(imc))
else:
    print('obesidade morbida, tu vai morrer ein')