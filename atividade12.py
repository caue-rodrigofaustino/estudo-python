#nesta atividade tive que analisar o começo do nome de uma cidade digitada
#usando um valor booleano TRUE ou False para caso a cidade tenha o primeiro nome santo ou nao respectivamente
cidade = str(input('digite a cidade: ')).strip()
print('sua cidade começa com santo? {}'.format(cidade[:5].upper() == 'SANTO'))