#criando classe conta bancaria

class Conta:
   def __init__(self, numero, cpf, nomeTitular, saldo ):
        self.numero = numero
        self.cpf = cpf
        self.nome = nomeTitular
        self.saldo = saldo

   def depositar(self, valor):
      self.saldo += valor

   def sacar(self, valor):
       if self.saldo < valor:
         return False
       else:
         self.saldo += valor
         return True

   def gerarExtrato(self):
      print(f'numero da conta:{self.numero}\nCPF:{self.cpf}\nNOME:{self.nome}\nSALDO:{self.saldo}')


c1 = Conta(11, 1263, 'carlo', 9000)
valor_saque = c1.sacar(12000)

if valor_saque:
  print('realizado com sucesso seu saque')
else:
  print('nao tem saldo o suficiente')
c1.gerarExtrato()
c1.depositar(1900)
c1.gerarExtrato()