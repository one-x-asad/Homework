class User():
    def __init__(self,ism,parol,email,email_paroli):
        self.ism=ism
        self.parol=parol
        self._email=email
        self.email_paroli=email_paroli
        
    def get_info(self):
        return self.ism,self.parol,self._email,self.email_paroli
    
    def get_ism(self):
        return self.ism
    
    def get_parol(self):
        return self.ism
    
a=User("Asadbek", 12345, "birbalo@gmail.com", 1234567)
b=User("Asadbek2", 123456, "birbalo2@gmail.com", 12345678)

print(a.get_info())
print(a.get_ism())
print(a.get_parol())

print(b.get_info())
print(b.get_ism())
print(b.get_parol())