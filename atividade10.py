nome = str(input('digita seu nome completo: '))

print('nome em maiusculo: {}'.format(nome.upper()))
print('nome em minusculo: {}'.format(nome.lower()))
print('nome sem espaços: {}'.format(len(nome) - nome.count(' ')))
print("primeiro nome tem: {} letras".format( len(nome.split()[0])))

nome= nome.split()

print('ultimo nome: {}'.format(nome[len(nome)-1]))

u = nome[len(nome)-1]

print('tem {} letras'.format(len(u)))