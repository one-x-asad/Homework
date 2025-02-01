class Telefon():
    def __init__(self,sifati,yogoch_turi,rangi,qalinligi):
        self.sifati=sifati
        self.yogoch_turi=yogoch_turi
        self.rangi=rangi
        self.qalinligi=qalinligi
    
    def get_info(self):
        return self.sifati,self.rangi,self.qalinligi,self.yogoch_turi
    
    def get_sifati(self):
        return self.sifati
    
    def get_yogoch_turi(self):
        return self.yogoch_turi
    
a=Telefon("yangi", "birch", "qora", "10SM")
b=Telefon("eski", "oak", "sariqroq", "2SM") 
c=Telefon("o'rtacha", "jungle", "oq", "5SM")       

print(a.get_info())
print(a.get_yogoch_turi())
print(a.get_sifati())

print(b.get_info())  
print(b.get_yogoch_turi())
print(b.get_sifati()) 

print(c.get_info()) 
print(c.get_yogoch_turi())
print(c.get_sifati())