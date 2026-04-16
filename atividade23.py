''' ver se e palindromo'''

fras = str(input("digite uma frase: ")).strip().upper()

palavra = fras.split()
'''transformando em vetor'''
junt = ''.join(palavra)
inverso = ''

for letra in range(len(junt) - 1, -1, -1):
  inverso += junt[letra]

print(junt, inverso)
if inverso == junt:
  print("temos um palindromo")
else:
  print("nao e um palindromo")