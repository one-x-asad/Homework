class Avtobus:
    def __init__(self, model, raqam, rang, olcham, ishlab_chiqaruvchi,yil="2024"):
        # Xususiyatlar
        self.model = model
        self.raqam = raqam
        self.rang = rang
        self.olcham = olcham
        self.ishlab_chiqaruvchi = ishlab_chiqaruvchi
        self._yil = yil


    def get_info(self):
      return self.model,self.raqam,self.rang,self.olcham,self.ishlab_chiqaruvchi,self._yil

    def get_model(self):
        return self.model

    def get_raqam(self):
        return self.raqam 
    
    def get_rang(self):
        return self.rang

a=Avtobus('Isuzu', '01A234', 'qizil', '12x3x4m', 'Isuzu Motors')
b=Avtobus('Mercedes', '02B567', 'yashil', '10x3x4m', 'Mercedes-Benz')
c=Avtobus('Volvo', '03C890', 'kok', '14x3x4.5m', 'Volvo Group')

print(a.get_info())
print(a.get_model())
print(a.get_raqam())
print(a.get_rang())

print(b.get_info())
print(b.get_model())
print(b.get_raqam())
print(b.get_rang())

print(c.get_info())
print(c.get_model())
print(c.get_raqam())
print(c.get_rang())