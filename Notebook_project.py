class Notebook():
    def __init__(self,xolati,rangi,rasmi,varaqlar_soni):
        self.xolati=xolati
        self.rangi=rangi
        self.rasmi=rasmi
        self.varaqlar_soni=varaqlar_soni
        
    def get_info(self):
        return self.xolati,self.rangi,self.rasmi,self.varaqlar_soni
    
    def get_xolati(self):
        return self.xolati
    
    def get_rangi(self):
        return self.rangi
    
a=Notebook("yangi", "qora", "mashina", 96)
b=Notebook("eski", "oq", "football", 48)      

print(a.get_info())
print(a.get_rangi())
print(a.get_xolati())

print(b.get_info())
print(b.get_rangi())
print(b.get_xolati())