import datetime

class person:
    def __init__(self,name,surname,birthdate,address,telephone,email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return "%s %s, born %s\nAddress: %s\nTelephone: %s\nEmail:%s" %(self.name,self.surname,self.birthdate,self.address,self.telephone,self.email)

Munna = person(
    'MD.Monirul Islam',
    'Munna',
    datetime.date(1998,2,2),
    "Munibpur,Pabna",
    '01784905235',
    'md.jovialmunna@gmail.com'

)

print(Munna)
print(Munna.__dict__)