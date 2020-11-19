''''
1. Rewrite the Person class so that a person’s age is calculated
for the ﬁrst time when a new person instance is created, and recalculated
(when it is requested) if the day has
changed since the last time that it was calculated.
'''
import datetime
class person:
    def __init__(self,name,surname,birthdate,address,telephone,email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

# This isn't strictly necessary, but it clearly introduces these attributes
        self._age = None
        self._age_last_recalculated = None
        self._recalculate_age()
    def _recalculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year,self.birthdate.month,self.birthdate.day):
            age -= 1
            self._age = age
            self._age_last_recalculated = today

    def age(self):
        if (datetime.date.today() > self._age_last_recalculated):
            self._recalculate_age()
            return self._age


person_1 = person(
    'MD.Monirul Islam',
    'Munna',
    datetime.date(1998,2,2), # year,month,day
    'Munibpur,Dogachi,Pabna',
    '01784905235',
    'md.jovialmunna@gmail.com'

)

print(person_1.name)
print(person_1.email)
person_1._recalculate_age()
print(person_1.age)



