import datetime # we will use this for date objects
class person:
    def __init__(self,name,surname,birthdate,address,telephone,email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year,self.birthdate.month,self.birthdate.day):
            age -= 1
        return age

person = person(
    'MD.Monirul Islam',
    'Munna',
    datetime.date(1998,2,2), # year,month,day
    'Munibpur,Dogachi,Pabna',
    '01784905235',
    'md.jovialmunna@gmail.com'

)

print(person.name)
print(person.email)
print(person.age())