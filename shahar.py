class Shahar():
    def __init__(self,nomi,rangi,uzunligi,kattaligi,bino_soni,bino_uzunligi):
        self.nomi=nomi
        self.rangi=rangi
        self.uzunligi=uzunligi
        self.bino_soni=bino_soni
        self.kattaligi=kattaligi
        self.bino_uzunligi=bino_uzunligi
        
    def info(self):
        return self.nomi,self.rangi,self.uzunligi,self.kattaligi,self.bino_soni,self.bino_uzunligi
    
    def get_rangi(self):
        return self.rangi
    
    def get_uzunligi(self):
        return self.uzunligi
    
class Hashar(Shahar):
    
    def get_nomi(self):
        return self.nomi

a1=Hashar("e1", "oq", "10Km", "180METR", 100, "10metr")
a2=Hashar("e2", "qora", "15KM", "150metr", 70, "20metr")

print(a1.info())
print(a1.get_rangi())
print(a1.get_uzunligi())
print(a1.get_nomi())

print(a2.info())
print(a2.get_rangi())
print(a2.get_uzunligi())
print(a2.get_nomi())