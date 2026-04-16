def main():
  print("digite seu texto. caso queira sair, digite 'sair' para terminar e salvar")
  frases = []

  while True:
    entrada = input("> ")
    if entrada.lower() == 'sair':
      break
    frases.append(entrada)


  with open("exemplo.txt", "w") as arquivo:
    for frase in frases:
      arquivo.write(frase + "\n")

  print("arquivo original criado com sucesso!")

  dados_mod = []

  with open("exemplo.txt", "r") as arquivo:
    for frase in arquivo:
      dados_mod.append(frase.strip().capitalize())

  with open("exemplo.txt", "w") as arquivo:
    for linha in dados_mod:
      arquivo.write(linha + "\n")
  print("dados sobescrittos com sucesso")

if __name__ == "__main__":
  main()