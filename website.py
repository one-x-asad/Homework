class Website():
    def __init__(self,nomi,rangi,uzunligi,kattaligi):
        self.nomi=nomi
        self.rangi=rangi
        self.uzunligi=uzunligi
        self.kattaligi=kattaligi
        
    def info(self):
        return self.nomi,self.rangi,self.uzunligi,self.kattaligi
    
    def get_rangi(self):
        return self.rangi
    
    def get_uzunligi(self):
        return self.uzunligi
    
    def get_kattaligi(self):
        return self.kattaligi
    
class Webnite(Website):
    
    def get_nomi(self):
        return self.nomi
    
a1=Webnite("food", "qora", "500px", "10sm")
a2=Webnite("cola", "qora", "300px", "15sm")

print(a1.info())
print(a1.get_rangi())
print(a1.uzunligi)
print(a1.get_kattaligi())
print(a1.get_nomi())

print(a2.info())
print(a2.get_rangi())
print(a2.uzunligi)
print(a2.get_kattaligi())
print(a2.get_nomi())