class myClass:
    class_attribute = 99

    def class_method(self):
        self.instance_attribute = 'I am instance attribute'


print(myClass.__dict__) 