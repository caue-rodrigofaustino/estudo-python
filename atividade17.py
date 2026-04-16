#nesta atividade utilizei um algoritimo para calcular se uma pessoa e capaz de comprar um imovel sem comprometer 30% do seu salario
imovel = float(input('digite o valor da casa: '))
salario = float(input('digite seu salario: '))
parcelas = int(input('digite quantos anos parcelados: '))

parc = imovel / (parcelas * 12)
minimo = (salario * 30) / 100


if parc <= minimo :
  print('sua compra da casa foi aprovada, pagando em {} anos com parcelas de R${:.2f}'.format(parcelas, parc))
else:
  print('sua compra foi negada, infelizmente a parcela {:.2f} ultrapassa 30% da sua renda'.format(parc))
print('para poder comprar tem que ganhar no minimo {}'.format(minimo))