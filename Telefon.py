class Telefon():
    def __init__(self,sifati,pamyati,rangi,kamerasi):
        self.sifati=sifati
        self.pamyati=pamyati
        self.rangi=rangi
        self.kamerasi=kamerasi
    
    def get_info(self):
        return self.sifati,self.rangi,self.pamyati,self.kamerasi
    
    def get_sifati(self):
        return self.sifati
    
    def get_pamyati(self):
        return self.pamyati
    
a=Telefon("yangi", "64GB", "qora", "108MP")
b=Telefon("eski", "32GB", "ko'k", "10MP") 
c=Telefon("o'rtacha", "128GB", "oq", "50MP")       

print(a.get_info())
print(a.get_pamyati())
print(a.get_sifati())

print(b.get_info())  
print(b.get_pamyati())
print(b.get_sifati()) 

print(c.get_info()) 
print(c.get_pamyati())
print(c.get_sifati())    