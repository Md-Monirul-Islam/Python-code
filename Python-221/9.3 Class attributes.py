class person:
    TITLE = ("Mr.",'Ms.','Mrs.','Dr.')
    def __init__(self,title,name,surname):
        if title not in self.TITLE:
            raise ValueError("%s is not a valid title." % title)
        self.title = title
        self.name = name
        self.surname = surname

# we can access a class attribute from an instance
person.TITLES

# but we can also access it from the class
Person.TITLES

# This will give us an error
person = person
Person.name
Person.surname