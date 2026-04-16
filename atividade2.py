#MEDIA ARITIMETICA
#primeiro capto os numeros digitados no input
n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

#crio uma variavel para somar os numeros, por ordem de prioridade, a soma acontece primeiro e logo apos a divisao por dois
med = (n1 + n2) / 2

#realizo a visualizaçao do resultado
print('media e {}'.format(med))