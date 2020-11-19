""""
1. Write a class for creating completely generic objects: its __init__
function should accept any number of
keyword parameters,and set the monthe object as attributes with the keys as names.
Writea __str__ method for the class – the string it returns should include the name
of the class and the values of all
the object’s custom instance attributes.
"""

class anyclass:
    def __init__(self,**kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        attrs = ["%s=%s" % (k, v) for (k, v) in self.__dict__.items()]
        classname = self.__class__.__name__
        return "%s: %s" % (classname, " ".join(attrs))

