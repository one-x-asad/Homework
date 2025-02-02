class Product():
    def __init__(self,tami,rangi,nomi,saqlanish_muddati,ishlab_chiqarilgan_sanasi="2025"):
        self.tami=tami
        self.rangi=rangi
        self.nomi=nomi
        self.saqlanish_muddati=saqlanish_muddati
        self.ishlab_chiqarilgan_sanasi=ishlab_chiqarilgan_sanasi
    
    def info(self):
        return self.tami,self.rangi,self.nomi,self.saqlanish_muddati,self.ishlab_chiqarilgan_sanasi
    
    def get_tami(self):
        return self.tami
    
    def get_rangi(self):
        return self.rangi
    
    def get_nomi(self):
        return self.nomi
    
a=Product("shirin", "qizil", "olma", "1oy")
b=Product("shirin", "sariq", "banan", "30kun")
c=Product("shirin", "qora", "chocacream", "2oy")
d=Product("nordon", "qizil", "anoq", "15kun")
e=Product("tamsiz", "saqiqroq", "non", "7kun")

print(a.info())
print(a.get_tami())
print(a.get_rangi())
print(a.get_nomi())

print(b.info())
print(b.get_tami())
print(b.get_rangi())
print(b.get_nomi())

print(c.info())
print(c.get_tami())
print(c.get_rangi())
print(c.get_nomi())

print(d.info())
print(d.get_tami())
print(d.get_rangi())
print(d.get_nomi())

print(e.info())
print(e.get_tami())
print(e.get_rangi())
print(e.get_nomi())