texto = "programaçao"
cont = "a"
contr = 0
#na posiçao letra coloca o tipo que procurar e texto aonde procurar

for numero in texto:
  if numero == cont:
    contr +=1
print('a letra {} aparece {} vezes em {}'.format(cont, contr, texto))
#o if e usado para aumenta contr, caso a logica seja concretizada
