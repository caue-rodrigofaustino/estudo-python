#criando lista e imprimindo
lista = [10, 20, 30, 40,50]
n1 = lista[0]
n2 = lista[1]
print(n1, n2)

#adicionando numero na lista ao final
lista.append(60)
print(lista)

#lista apos adicionar numero em especifico
lista.insert(1,25)
print(f'{lista}\n')

#removendo elemento
lista.remove(40)
print(lista)

#removendo ultimo elemento
ultim = lista.pop()
print(ultim)#elemento removido
print('apos remover ultimo elemento')
print(lista)#apos remover o ultimo elemento

#acessando um subgrup
sub = lista[1:4]
print(f'{sub}\n')

#criando um dicionario
dicionario = {
    'nome': 'caue rodrigo',
    'idade': 25,
    'cidade': 'sao jose'
}

#criando acesso aos elementos do dicionario
n = dicionario['nome']
i = dicionario['idade']
c = dicionario['cidade']

print('dicionario')
print(f'{n}\n{i}\n{c}\n')

#adicionando um novo valor no dicionario
dicionario['profissao'] = 'professor'
dicionario['idade'] = 22
print(dicionario)