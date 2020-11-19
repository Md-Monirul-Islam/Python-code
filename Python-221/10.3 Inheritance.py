class person:
    def __init__(self,name,surname,number):
        self.name = name
        self.surname = surname
        self.number = number
class students(person):
    UNDERGRADUATE, POSTGRADUATE = range(2)
    def __init__(self,student_type, *args,**kwargs):
        self.student_type = student_type
        self.classes = []
        super(students,self).__init__(*args,**kwargs)

    def enrol(self,course):
        self.classes.append(course)

class staffMember(person):
    PERMANENT,TEMPORARY = range(2)
    def __init__(self,empolyee_type,*args,**kwargs):
        self.empolyee_type = empolyee_type
        super(staffMember,self).__init__(*args,**kwargs)

class lecturer(staffMember):
    def __init__(self,*args,**kwargs):
        staffMember.courses_taught = []
        super(lecturer,self).__init__(*args,**kwargs)

    def assign_teaching(self,courses):
        self.courses_taught.append(courses)

Munna = students(students.POSTGRADUATE,"Monirul","Munna","SMTJNX045")
print(Munna.enrol('a_postgrad_course'))
Maznu = lecturer(staffMember.PERMANENT,"Maznu","PK","01784905235")
print(Maznu.assign_teaching('an_undergrad_course'))
