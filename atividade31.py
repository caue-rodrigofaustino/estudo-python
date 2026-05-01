num = int(input("digite um número:"))
resultado = 1
contador = num
#mostra o numero!
print("{}! = ".format(num), end='')

while contador > 0:
    #esse print mostra o numero que ira iniciar a multiplicaçao
    print("{}".format(contador), end='')
    #esse print utiliza um if dentro para imprimir um x ou = 
    print(' x ' if contador > 1 else ' = ', end='')
    resultado *= contador
    contador -= 1


print("{}".format(resultado))
