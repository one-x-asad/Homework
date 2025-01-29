class Uy():
    def __init__(self,razmer,yili,shinamligi,vidi,narsalari):
        self.razmer=razmer
        self.yili=yili
        self.shinamligi=shinamligi
        self.vidi=vidi
        self.narsalari=narsalari
        
    def get_info(self):
        return self.razmer,self.yili,self.shinamligi,self.vidi,self.narsalari
    
    def get_razmer(self):
        return self.razmer
    
    def get_yili(self):
        return self.yili
    
    def get_shinamligi(self):
        return self.shinamligi
    
a=Uy("katta", 2020, "qulay", "chiroyli", "jihozlangan")
b=Uy("kichik", 2015, "noqulay", "bo'qrang", "jihozlanmagan")
c=Uy("o'rtancha", 2017, "mazza", "qora_rangli", "ko'p_narsa")
d=Uy("juda_kichik", 2010, "o'tirishag_qo'rqadigan_darajada", "normal", "kam_narsa")

print(a.get_info())
print(a.get_razmer())
print(a.get_shinamligi())
print(a.get_yili())
c
print(b.get_info())
print(b.get_razmer())
print(b.get_shinamligi())
print(b.get_yili())

print(c.get_info())
print(c.get_razmer())
print(c.get_shinamligi())
print(c.get_yili())

print(d.get_info())
print(d.get_razmer())
print(d.get_shinamligi())
print(d.get_yili())