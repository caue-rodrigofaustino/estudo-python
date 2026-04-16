#achar uma letra
frase = str(input('digite: ')).lower().strip()
print('letra A apareceu {} vezes'.format(frase.count('a')))
print('letra A apareceu na posiçao {} na primeira vez'.format(frase.find('a') + 1))
print('letra A apareceu ultima vez na posiçao {}'.format(frase.rfind('a') + 1))