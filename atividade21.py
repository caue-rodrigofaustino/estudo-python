class Televisao:
    def __init__(self, canal,  cMin, cMax):
       self.canal = canal
       self.min = cMin
       self.max = cMax

    def muda_canal_baixo(self):
        if self.canal - 1 >= self.min:
          self.canal -= 1
        else:
            self.canal = self.max

    def muda_canal_cima(self):
        if self.canal + 1 <= self.max:
            self.canal += 1
        else:
            self.canal = self.min


tev1 = Televisao( 3 , 2 , 10 )

print(tev1.canal)
tev1.muda_canal_baixo()
print(tev1.canal)
tev1.muda_canal_baixo()
print(tev1.canal)